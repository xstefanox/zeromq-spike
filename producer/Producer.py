from random import random
from time import sleep

import zmq
from zmq import Socket, PUSH, ZMQError

from producer.logger import log


class Producer:
    producing: bool = True
    socket: Socket = None

    def run(self):
        log.info("starting")

        context = zmq.Context()

        with context.socket(PUSH) as self.socket:
            self.socket.bind("tcp://*:5555")

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

        log.info("terminating")

    def stop_producing(self):
        self.producing = False
        self.socket.close()
