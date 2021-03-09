import os
from signal import signal, SIGINT

from consumer.Consumer import Consumer

if __name__ == "__main__":
    producer_host = os.environ.get("PRODUCER_HOST") or "localhost"
    producer_port = os.environ.get("PRODUCER_PORT") or "5555"
    consumer = Consumer(producer_host, producer_port)
    signal(SIGINT, lambda signum, frame: consumer.stop_consuming())
    consumer.run()
