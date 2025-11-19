import pytest
from src.services.queue.manager import execute


def test_execute_ok(capsys):
    execute("send_notification", {"msg": "hello"})
    captured = capsys.readouterr()
    assert "NOTIFY" in captured.out


def test_execute_unknown():
    with pytest.raises(ValueError):
        execute("unknown_task", {})
