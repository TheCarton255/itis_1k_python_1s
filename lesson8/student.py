class student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    def info(self):
        return f"{self.name} ({self.group}): {self.average()}"