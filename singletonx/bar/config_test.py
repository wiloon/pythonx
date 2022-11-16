from config import AppConfig


def main():
    cls1 = AppConfig()
    cls1.get()
    cls2 = AppConfig()
    cls1.get()
    print(id(cls1) == id(cls2))


if __name__ == '__main__':
    main()
