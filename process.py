from time import sleep
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def process_work(counter, random_number):
    sleep_time = int(random_number/100)
    logger.info(f"{counter} Worker is processing {random_number}")
    logger.info(f"{counter} Worker sleeping for {sleep_time}")
    sleep(sleep_time)
    logger.info(f"{counter} Finished {random_number}")
    return sleep_time
