import threading
from typing import Any


class Applier:

    def apply(self, value: Any) -> Any:
        pass


class SingletonMeta(type):
    __instances = {}
    __singleton_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls.__singleton_lock:
            if cls not in cls.__instances:
                instance = super().__call__(*args, **kwargs)
                cls.__instances[cls] = instance
            return cls.__instances[cls]
