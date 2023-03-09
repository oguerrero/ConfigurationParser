import os

from helpers.Utils import print_root
from parser.ConfigParser import ConfigParser
from parser.Menu import menu


def main():
    config_parser = ConfigParser()

    config_file_path = input("Please enter the path to the config file: ")

    while not os.path.isfile(config_file_path):  # Validate if the path is a file
        config_file_path = input("The path you entered is not a file. Please enter a valid path: ")

    config_parser.parse(config_file_path)  # Parse the config file
    print_root(config_parser)  # Print the tree of the config file

    print("To access a property, please enter the path of the section")
    print("example: runtime.system1.subsystem1")

    menu(config_parser)  # Menu to navigate through the config file


if __name__ == "__main__":
    main()

