class DataSource:

    def __init__(self, data):
        self.lines = data.split()
        self.lineCount = len(self.lines)
        self.index = 0
        self.line = ""

    def __iter__(self):
        return self

    def __next__(self):
        if (self.index + 1 > self.lineCount):
            raise StopIteration()
        line = self.lines[self.index]
        line = line.strip()
        self.index = self.index + 1
        return line


