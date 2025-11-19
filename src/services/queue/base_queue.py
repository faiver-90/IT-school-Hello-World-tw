from queue import Queue
from threading import Lock

main_queue = Queue()
processing = {}
dead = []

lock = Lock()

RETRY_LIMIT = 3
