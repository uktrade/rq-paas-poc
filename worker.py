from redis import Redis
from rq import Worker

import os
import sys
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

logger.info(f'REDIS_BASE_URL (partial): {REDIS_BASE_URL[:11]}...')
logger.info(f'Args: {len(sys.argv)}')

if len(sys.argv) >= 2:
    queue = sys.argv[1]
else:
    queue = 'default'

logger.info(f'Queue: {queue}')

worker = Worker(queue, connection=Redis.from_url(REDIS_BASE_URL))
worker.work()
