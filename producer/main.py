import os
from signal import signal, SIGINT

from producer.Producer import Producer

if __name__ == "__main__":
    port = os.environ.get("PORT") or "5555"
    producer = Producer(port)
    signal(SIGINT, lambda signum, frame: producer.stop_producing())
    producer.run()
