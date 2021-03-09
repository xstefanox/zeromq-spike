from signal import signal, SIGINT

from producer.Producer import Producer

if __name__ == "__main__":
    producer = Producer()
    signal(SIGINT, lambda signum, frame: producer.stop_producing())
    producer.run()
