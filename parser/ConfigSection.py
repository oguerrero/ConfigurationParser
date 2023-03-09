class ConfigSection:
    def __init__(self, name, parent=None):
        self.name = name
        self.values = {}
        self.flags = set()
        self.subsections = []
        self.parent = parent

    def get(self, key, default=None):
        return self.values.get(key, default)

    def get_flag(self, flag):
        return flag in self.flags   

    def get_subsection(self, name):
        for subsection in self.subsections:
            if subsection.name == name:
                return subsection
        return None

    def get_subsections_name(self):
        return [subsection.name for subsection in self.subsections]

    def __str__(self):
        return f"<ConfigSection name={self.name} values={self.values} flags={self.flags} " \
               f"subsections={self.subsections}>"
