import unittest

from parser.ConfigParser import ConfigParser


class TestPathFile(unittest.TestCase):
    def test_valid_config_file(self):
        config_parser = ConfigParser()
        config_parser.parse("txt/test.txt")

        # Test the parsed sections
        runtime_section = config_parser.get_section("runtime")
        self.assertEqual(runtime_section.get_subsections_name(), ['system1', 'system2'])

    def test_invalid_config_file(self):
        config_parser = ConfigParser()

        # Test parsing an invalid config file
        with self.assertRaises(Exception):
            config_parser.parse("test_invalid_config_file.txt")


if __name__ == '__main__':
    unittest.main()
