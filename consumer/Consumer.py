import zmq
from zmq import Socket, PULL, ZMQError

from producer.logger import log


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
                    message = self.socket.recv()
                    log.debug("consuming message [%s]" % message)
                except ZMQError as e:
                    if e.errno == zmq.ENOTSOCK:
                        log.debug("socket has been closed")
                    else:
                        log.error(e)

        log.info("terminating consumer")

    def stop_consuming(self):
        self.consuming = False
        self.socket.close()
