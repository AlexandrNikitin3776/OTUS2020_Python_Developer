import unittest
from unittest import mock

from log_analyzer import parse_config_path, DEFAULT_CONFIG_PATH


class TestParseConfig(unittest.TestCase):
    def test_parse_config_path(self):
        test_config_path = './some_config_path.txt'
        with mock.patch('sys.argv', ['', '--config', test_config_path]):
            self.assertEqual(parse_config_path(), test_config_path)

    def test_parse_default_config_path(self):
        with mock.patch('sys.argv', ['']):
            self.assertEqual(parse_config_path(), DEFAULT_CONFIG_PATH)


if __name__ == '__main__':
    unittest.main()
