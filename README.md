# rq-paas-poc

Simple app to test the principles of RQ when deployed to Gov Paas.

The worker can be run with no parameters, which will serve the 'default' queue:  
- `python worker.py`

Or can run with another queue, for example:
- `python worker.py short-running-queue`
- `python worker.py long-running-queue`

Or multiple workers can be running, serving different queues.


The "web" (not a real web) process can be configured with env vars:
- `RQPOC_QUEUE_NAME` - name of the queue. Defaults to "default" but can be set to match the worker(s).
- `RQPOC_MAX_RANDOM` - Used together with the sleep var. This is the random number sent to the worker, and also how long the worker will sleep for (1000=10 seconds). Default is 1000.
- `RQPOC_SLEEP` - This defines how long the web will sleep for (i.e. how often it generates some work for the worker). Default is 5 seconds.

Hence, the default of the web generating every 5 seconds and the worker sleeping (simulating 'working') for between 0 and 9 - the processes should run out of step - but on average the worker should keep up.

Other scenarios can be configured as required.
