import json

import zmq
from zmq import Socket, PULL, ZMQError

from logger.logger import log


class Consumer:
    producer_host: str = None
    producer_port: int = None
    consuming: bool = True
    socket: Socket = None

    def __init__(self, producer_host, producer_port):
        self.producer_host = producer_host
        self.producer_port = producer_port

    def run(self):
        log.info(f"starting consumer, connecting to {self.producer_host}:{self.producer_port}")

        context = zmq.Context()

        with context.socket(PULL) as self.socket:
            self.socket.connect(f"tcp://{self.producer_host}:{self.producer_port}")

            while self.consuming:
                try:
                    # noinspection PyUnresolvedReferences
                    message = json.loads(self.socket.recv().decode("utf-8"))
                    log.debug("consuming message: %s %s" % (message["text"], message["value"]))
                except ZMQError as e:
                    if e.errno == zmq.ENOTSOCK:
                        log.debug("socket has been closed")
                    else:
                        log.error(e)

        log.info("terminating consumer")

    def stop_consuming(self):
        self.consuming = False
        self.socket.close()
