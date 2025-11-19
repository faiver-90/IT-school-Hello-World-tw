from src.services.queue.base_queue import main_queue, TaskItem


def test_enqueue_basic():
    item: TaskItem = {
        "task": "send_notification",
        "payload": {"student_id": 1},
        "attempt": 0,
    }
    main_queue.put(item)
    assert not main_queue.empty()

    pulled = main_queue.get()
    assert pulled["task"] == "send_notification"
