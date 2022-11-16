from threading import Lock
from kafka import KafkaProducer
import time


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class KafkaProducer(metaclass=SingletonMeta):
    producer = None
    """
    We'll use this property to prove that our Singleton really works.
    """

    def __init__(self, value: str) -> None:
        self.value = value
        print("kafka producer init")
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        print(id(self.producer))

    def send(self, topic, key, value):
        print(id(self.producer))
        self.producer.send(topic, key=(bytes(key, encoding="utf8")), value=(bytes(value, encoding="utf8")))
        print("data sent, value: " + value)


def test_singleton(value: str) -> None:
    foo = KafkaProducer(value)
    foo.send("topic0", "k0", "v0")
    bar = KafkaProducer(value)
    bar.send("topic0", "k1", "v1")
    time.sleep(3)


if __name__ == "__main__":
    test_singleton('')
