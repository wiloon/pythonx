class Foo(object):
    def __init__(self):
        self.field0 = 0
        self.field1 = None

    def exec(self):
        print(self.field0)


class Bar(Foo):
    def __init__(self):
        super().__init__()
        self.field0 = 1
        self.field1 = ['key0']


if __name__ == '__main__':
    b = Bar()
    print(b.field0)
    b.exec()
