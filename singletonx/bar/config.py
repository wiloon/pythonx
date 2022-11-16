from threading import Lock


class MetaClass(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class AppConfig(metaclass=MetaClass):
    loaded_obj = None

    def __init__(self) -> None:
        self.loaded_obj = "foo"
        print("init")

    def get(self):
        print(self.loaded_obj)
