from src.services.queue.base_queue import main_queue, dead
from src.services.queue.worker import Worker


def failing_task(_):
    raise RuntimeError("fail")


def test_worker_retry(monkeypatch):
    from src.services.queue import manager

    manager.TASKS["fail_task"] = failing_task

    item = {
        "task": "fail_task",
        "payload": {},
        "attempt": 0,
    }
    main_queue.put(item)

    worker = Worker()
    worker.daemon = True

    # Запустим один цикл исполнения вручную
    import threading
    import time

    t = threading.Thread(target=worker.run, daemon=True)
    t.start()

    time.sleep(0.5)

    # После 3 попыток задача должна попасть в dead
    assert len(dead) == 1
    assert dead[0]["task"] == "fail_task"
