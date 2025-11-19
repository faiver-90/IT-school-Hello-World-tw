from queue import Queue
from threading import Lock
from typing import Dict, Any, TypedDict, List


class TaskItem(TypedDict):
    task: str
    payload: Dict[str, Any]
    attempt: int


main_queue: "Queue[TaskItem]" = Queue()

processing: Dict[int, TaskItem] = {}

dead: List[TaskItem] = []

lock = Lock()

RETRY_LIMIT: int = 3
