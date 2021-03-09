from random import random

import zmq
from zmq import Socket, PUSH, ZMQError

from producer.logger import log


class Producer:
    producing: bool = True
    socket: Socket = None
    port: int = None

    def __init__(self, port):
        self.port = port

    def run(self):
        log.info(f"starting producer, listening on port {self.port}")

        context = zmq.Context()

        with context.socket(PUSH) as self.socket:
            self.socket.bind(f"tcp://*:{self.port}")

            while self.producing:
                message = f"hello world ({random()}"
                log.debug("producing message [%s]" % message)
                try:
                    self.socket.send(bytes(message, 'UTF-8'))
                except ZMQError as e:
                    if e.errno == zmq.ENOTSOCK:
                        log.debug("socket has been closed, terminating")
                    else:
                        log.error(e)

        log.info("terminating producer")

    def stop_producing(self):
        self.producing = False
        self.socket.close()
