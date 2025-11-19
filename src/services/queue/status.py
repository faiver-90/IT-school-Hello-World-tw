from .base_queue import processing, dead


def get_processing():
    return list(processing.values())


def get_dead():
    return dead
