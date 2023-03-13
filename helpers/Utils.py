def print_section_info(section):
    print()
    print("========VALUES=======")
    for value in section.values:
        print(value)
    print("========FLAGS========")
    for flag in section.flags:
        print(flag)
    print("=====SUBSECTIONS=====")
    for subsection in section.subsections:
        print(subsection)
    print("=====================")
    print()


def print_root(config_parser, section=None, indent=0):
    if section is None:
        section = config_parser.root_section

    print(" " * indent + section.name)

    for subsection_name in section.subsections:
        subsection = section.subsections[subsection_name]
        print_root(config_parser, subsection, indent=indent + 2)


def print_values(section):
    print()
    print("========VALUES=======")
    for value in section.values:
        print(value)
    print("=====================")
    print()


def print_flags(section):
    print()
    print("========FLAGS========")
    for flag in section.flags:
        print(flag)
    print("=====================")
    print()


def print_subsections(section):
    print()
    print("=====SUBSECTIONS=====")
    for subsection in section.subsections:
        print(subsection)
    print("=====================")
    print()
