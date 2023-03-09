import unittest

from parser.ConfigParser import ConfigParser


class MyTestCase(unittest.TestCase):
    config_parser = ConfigParser()
    config_parser.parse("txt/test2.txt")

    def test_root_section(self):
        runtime_section = self.config_parser.get_section("runtime")

        self.assertEqual(runtime_section.get("key1"), "value1")
        self.assertEqual(runtime_section.get("key2"), "value2")
        self.assertEqual(runtime_section.get_flag("flag1"), True)

    def test_deep_subsystem(self):
        subsystem1_section = self.config_parser.get_section("runtime.system2.subsystem1.subsystem2")

        self.assertEqual(subsystem1_section.get("prop3"), ['value1', 'value2', 'value3'])
        self.assertEqual(subsystem1_section.get_flag("flag2"), True)


if __name__ == '__main__':
    unittest.main()
