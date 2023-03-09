import re

from parser.ConfigSection import ConfigSection


class ConfigParser:
    def __init__(self):
        self.root_section = ConfigSection("")
        self.current_section = self.root_section
        self.stack = [self.current_section]

    def parse(self, filename):
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                # Check if line is a section header
                match = re.match(r"^\s*(\w+)\s*{", line)
                if match:
                    section_name = match.group(1)
                    self.current_section = ConfigSection(section_name, parent=self.stack[-1])
                    self.stack[-1].subsections.append(self.current_section)
                    self.stack.append(self.current_section)
                    continue

                # Check if line is a closing section brace
                if line == "}":
                    self.stack.pop()
                    self.current_section = self.stack[-1]
                    continue

                # Parse key-value pairs and flags
                line = line.replace("{", "")
                line = line.replace("}", "")
                parts = line.split()
                if len(parts) == 1:
                    self.current_section.flags.add(parts[0])
                elif len(parts) == 2:
                    self.current_section.values[parts[0]] = parts[1]
                else:
                    self.current_section.values[parts[0]] = parts[1:]

    def get_section(self, name):
        if not name:
            return self.root_section
        parts = name.split(".")
        section = self.root_section
        for part in parts:
            section = section.get_subsection(part)
            if not section:
                return None
        return section

    def __str__(self):
        return f"<ConfigParser root_section={self.root_section}>"
