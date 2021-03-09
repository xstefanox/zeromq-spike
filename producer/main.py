import logging
import sys
from random import random
from signal import signal, SIGINT

import zmq
from zmq import PUSH, Socket, ZMQError

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(processName)s - %(levelname)s - %(message)s'))

log = logging.getLogger(__name__)
log.addHandler(log_handler)
log.setLevel(logging.DEBUG)


class Producer:
    producing: bool = True
    socket: Socket = None

    def run(self):
        log.info("starting")

        context = zmq.Context()

        with context.socket(PUSH) as socket:
            self.socket = socket
            socket.bind("tcp://*:5555")

            while self.producing:
                message = f"hello world ({random()}"
                log.debug("producing message [%s]" % message)
                try:
                    socket.send(bytes(message, 'UTF-8'))
                except ZMQError as e:
                    if e.errno == zmq.ENOTSOCK:
                        log.debug("socket has been closed, terminating")
                    else:
                        log.error(e)

        log.info("terminating")

    def stop_producing(self):
        self.producing = False
        self.socket.close()


if __name__ == "__main__":
    producer = Producer()
    signal(SIGINT, lambda signum, frame: producer.stop_producing())
    producer.run()
