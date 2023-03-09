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
        print(subsection.name)
    print("=====================")
    print()


def print_root(config_parser):
    print("========TREE=========")
    for section in config_parser.root_section.subsections:
        print(section.name)
        for subsection in section.subsections:
            print(f'\t{subsection.name}')
            for subsubsection in subsection.subsections:
                print(f'\t\t{subsubsection.name}')
                for subsubsubsection in subsubsection.subsections:
                    print(f'\t\t\t{subsubsubsection.name}')
    print("=====================")


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
        print(subsection.name)
    print("=====================")
    print()
