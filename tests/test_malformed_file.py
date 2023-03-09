import unittest

from parser.ConfigParser import ConfigParser


class TestMalformedFile (unittest.TestCase):
    config_parser = ConfigParser()
    config_parser.parse("txt/test4.txt")

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


if __name__ == '__main__':
    unittest.main()
