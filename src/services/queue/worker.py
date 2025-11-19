import time
from threading import Thread

from .base_queue import (
    main_queue,
    processing,
    dead,
    lock,
    RETRY_LIMIT,
    TaskItem,
)
from .manager import execute


class Worker(Thread):
    daemon: bool = True

    def run(self) -> None:
        print("Worker started")

        while True:
            item: TaskItem = main_queue.get()

            task: str = item["task"]
            payload = item["payload"]
            attempt: int = item["attempt"] + 1

            with lock:
                processing[id(item)] = item

            try:
                execute(task, payload)

                with lock:
                    processing.pop(id(item), None)

                print(f"[OK] {task}")

            except Exception as e:
                print(f"[ERR] {task} attempt {attempt}: {e}")

                with lock:
                    processing.pop(id(item), None)

                if attempt < RETRY_LIMIT:
                    item["attempt"] = attempt
                    main_queue.put(item)
                else:
                    dead.append(item)
                    print(f"[DEAD] {task}")

            time.sleep(0.1)
