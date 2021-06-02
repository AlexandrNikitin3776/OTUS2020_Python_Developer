import unittest
from unittest import mock


class TestArgs(unittest.TestCase):
    def test_ok(self):
        with mock.patch('sys.argv', ['-f']):
            pass

if __name__ == '__main__':
    unittest.main()
