# ruff: noqa: E402
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

from src.services.queue.base_queue import main_queue, processing, dead

import pytest


@pytest.fixture(autouse=True)
def clear_queue():
    while not main_queue.empty():
        main_queue.get()

    processing.clear()
    dead.clear()

    yield
