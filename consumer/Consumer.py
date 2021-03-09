import zmq
from zmq import Socket, PULL, ZMQError, ENOTSOCK, RCVTIMEO, EAGAIN

from logger.logger import log


class Consumer:
    producer_host: str = None
    producer_port: int = None
    consuming: bool = True
    socket: Socket = None

    def __init__(self, producer_host, producer_port, receive_timeout_ms):
        self.producer_host = producer_host
        self.producer_port = producer_port
        self.receive_timeout_ms = receive_timeout_ms

    def run(self):
        log.info(f"starting consumer, connecting to {self.producer_host}:{self.producer_port}")

        context = zmq.Context()

        with context.socket(PULL) as self.socket:
            self.socket.setsockopt(RCVTIMEO, self.receive_timeout_ms)
            self.socket.connect(f"tcp://{self.producer_host}:{self.producer_port}")

            while self.consuming:
                try:
                    message = self.socket.recv_json()
                    log.debug("consuming message: %s %s" % (message["text"], message["value"]))
                except ZMQError as e:
                    if e.errno == ENOTSOCK:
                        log.debug("socket has been closed")
                    elif e.errno == EAGAIN:
                        log.info(
                            f"no message received for %s ms, assuming producer has shutdown" % self.receive_timeout_ms
                        )
                        break
                    else:
                        log.error(e)
                        log.error(e.errno)

        log.info("terminating")
        context.term()

    def stop_consuming(self):
        self.consuming = False
        self.socket.close()
