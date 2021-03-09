import logging
import sys

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

log = logging.getLogger(__name__)
log.addHandler(log_handler)
log.setLevel(logging.DEBUG)
