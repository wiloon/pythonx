import unittest

from kafkax import send_to_kafka


class TestKafka(unittest.TestCase):

    def test_send(self):
        send_to_kafka("foo")


if __name__ == '__main__':
    unittest.main()