import unittest

from parser.ConfigParser import ConfigParser


class TestExample(unittest.TestCase):
    config_parser = ConfigParser()
    config_parser.parse("txt/test.txt")

    def test_root_section(self):
        runtime_section = self.config_parser.get_section("runtime")

        self.assertEqual(runtime_section.get("key1"), "value1")
        self.assertEqual(runtime_section.get("key2"), "value2")
        self.assertEqual(runtime_section.get_flag("flag1"), True)

    def test_sub_section(self):
        system1_section = self.config_parser.get_section("runtime.system1")

        self.assertEqual(system1_section.get("prop1"), "value1")
        self.assertEqual((system1_section.get("prop2")), "value2")
        self.assertEqual(system1_section.get("ports"), ['1234', '5678', '9102'])

    def test_sub_sub_section(self):
        subsystem1_section = self.config_parser.get_section("runtime.system1.subsystem1")

        self.assertEqual(subsystem1_section.get("prop3"), ['value1', 'value2', 'value3'])
        self.assertEqual(subsystem1_section.get_flag("flag2"), True)


if __name__ == '__main__':
    unittest.main()
