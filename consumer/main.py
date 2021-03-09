from signal import signal, SIGINT

from consumer.Consumer import Consumer

if __name__ == "__main__":
    consumer = Consumer()
    signal(SIGINT, lambda signum, frame: consumer.stop_consuming())
    consumer.run()
