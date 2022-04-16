import uuid


def get_random_id(len=10):
    return uuid.uuid4().hex[:len].upper()
