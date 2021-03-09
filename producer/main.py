import logging
import sys

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(processName)s - %(levelname)s - %(message)s'))

log = logging.getLogger(__name__)
log.addHandler(log_handler)
log.setLevel(logging.DEBUG)


def produce():
    log.info("starting")
    log.info("terminating")


if __name__ == "__main__":
    produce()
