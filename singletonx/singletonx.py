class MetaCls(type):
    _instances = {}

    def __new__(cls, name, bases, newattrs):
        print("new: %r" % (name))

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaCls, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cls4(metaclass=MetaCls):

    def __init__(self) -> None:
        print("cls init")

    def send(self, msg):
        print("send: " + msg)


def main():
    cls1 = Cls4()
    cls1.send("foo")
    cls2 = Cls4()
    cls1.send("bar")
    print(id(cls1) == id(cls2))


if __name__ == '__main__':
    main()
