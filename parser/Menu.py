from helpers.Utils import print_section_info, print_subsections, print_flags, print_values


def print_value(section):
    print_values(section)

    property_name = input("Please enter the name of the property you want to get: ")
    value_property = section.get(property_name)

    if not value_property:
        print("The value does not exist")
    else:
        print(f'{property_name} = {value_property}')


def print_flag(section):
    print_flags(section)

    property_name = input("Please enter the name of the property you want to get: ")
    flag_property = section.get_flag(property_name)

    if not flag_property:
        print("The flag does not exist")
    else:
        print(f'{property_name} = {flag_property}')


def print_subsection(section):
    print_subsections(section)

    property_name = input("Please enter the name of the property you want to get: ")
    section_property = section.get_subsection(property_name)

    if not section_property:
        print("The subsection does not exist")
    else:
        print_section_info(section_property)


def menu(config_parser):
    while True:
        section_name = input(
            "Please enter the path of the section you want to get or type exit to close the parser: ")

        if section_name == "exit":
            break

        section = config_parser.get_section(section_name)

        if section:
            print_section_info(section)  # Print the tree of the section

            print("What are you looking for?: "
                  "\n1. values"
                  "\n2. flags"
                  "\n3. subsections")
            option = int(input("> "))

            if option == 1:
                if len(section.values) == 0:
                    print("The section does not have values")
                    continue

                print_value(section, )
            elif option == 2:
                if len(section.flags) == 0:
                    print("The section does not have flags")
                    continue

                print_flag(section, )
            elif option == 3:
                if len(section.subsections) == 0:
                    print("The section does not have subsections")
                    continue

                print_subsection(section, )
            else:
                print("The option does not exist")
        else:
            print("The section does not exist")
