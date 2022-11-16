from datetime import datetime

if __name__ == '__main__':
    s = '2022-02-10 03:11:03.562198'
    d = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")
    print("---")
    print(d)

    s = '2022-02-10 03:11:03.562198+0000'
    d = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f%z")
    print("---")
    print(d)

    s = '2022-02-10 03:11:03.562198+00'
    d = datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f%z")
    print("---")
    print(d)