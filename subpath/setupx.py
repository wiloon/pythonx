import os
import sys

if __name__ == '__main__':
    print("start...")

    require_file = path = '%s%s%s' % (
        os.path.dirname(os.path.abspath(__file__)),
        os.sep,
        "../requirements.txt"
    )

    print("---")

    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.sep)
    print(path)

    print("sys platform: ", sys.platform.lower())
