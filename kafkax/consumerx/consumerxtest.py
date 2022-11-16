import unittest

from consumerx import consume_topic0


class TestKafka(unittest.TestCase):

    def test_send(self):
        consume_topic0()


if __name__ == '__main__':
    unittest.main()
