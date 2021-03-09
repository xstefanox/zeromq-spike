import os
from signal import signal, SIGINT, SIGTERM

from consumer.Consumer import Consumer

if __name__ == "__main__":
    producer_host = os.environ.get("PRODUCER_HOST") or "localhost"
    producer_port = os.environ.get("PRODUCER_PORT") or "5555"
    receive_timeout_ms = os.environ.get("RECEIVE_TIMEOUT_MS") or 5000
    consumer = Consumer(producer_host, producer_port, receive_timeout_ms)
    signal(SIGINT, lambda signum, frame: consumer.stop_consuming())
    signal(SIGTERM, lambda signum, frame: consumer.stop_consuming())
    consumer.run()
