import zmq
from zmq import Socket, PULL, ZMQError

from producer.logger import log


class Consumer:
    consuming: bool = True
    socket: Socket = None

    def run(self):
        log.info("starting")

        context = zmq.Context()

        with context.socket(PULL) as self.socket:
            self.socket.connect("tcp://localhost:5555")

            while self.consuming:
                try:
                    message = self.socket.recv()
                    log.debug("consuming message [%s]" % message)
                except ZMQError as e:
                    if e.errno == zmq.ENOTSOCK:
                        log.debug("socket has been closed")
                    else:
                        log.error(e)

        log.info("terminating")

    def stop_consuming(self):
        self.consuming = False
        self.socket.close()
