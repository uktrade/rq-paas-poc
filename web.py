from process import process_work

from redis import Redis
from rq import Queue

from time import sleep
from numpy import random
import os
import logging
import json


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

VCAP_SERVICES = os.environ.get('VCAP_SERVICES', default={})
logger.info(f'VCAP_SERVICES (partial): {VCAP_SERVICES[:50]}...')

if 'redis' in VCAP_SERVICES:
    REDIS_BASE_URL = json.loads(VCAP_SERVICES)['redis'][0]['credentials']['uri']
else:
    REDIS_BASE_URL = "redis://localhost:6379"

RQPOC_QUEUE_NAME = os.environ.get('RQPOC_QUEUE_NAME', default="default")
RQPOC_MAX_RANDOM = os.environ.get('RQPOC_MAX_RANDOM', default=1000)
RQPOC_SLEEP = os.environ.get('RQPOC_SLEEP', default=5)

logger.info(f'REDIS_BASE_URL (partial): {REDIS_BASE_URL[:11]}...')
logger.info(f'RQPOC_QUEUE_NAME: {RQPOC_QUEUE_NAME}')
logger.info(f'RQPOC_MAX_RANDOM: {RQPOC_MAX_RANDOM}')
logger.info(f'RQPOC_SLEEP: {RQPOC_SLEEP}')

queue = Queue(name = RQPOC_QUEUE_NAME, connection=Redis.from_url(REDIS_BASE_URL))
counter = 0

while True:
    random_number = random.randint(RQPOC_MAX_RANDOM)
    logger.info(f'{counter} Web work number {random_number}')
    job = queue.enqueue(process_work, counter, random_number)
    logger.info(f'{counter} Web sleeping for {RQPOC_SLEEP}')
    sleep(RQPOC_SLEEP)
    counter+=1
