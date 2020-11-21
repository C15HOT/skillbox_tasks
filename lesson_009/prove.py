class Parser:

    def __init__(self, filename):
        self.filename = filename
        self.stat = {}
        self.right = 17

    def collect(self):
        with open(file=self.filename, mode='r', encoding='utf8') as file:
            for line in file:
                self.line_stat(line)

    def line_stat(self, line):
        if 'NOK' in line:
            key = line[0:self.right]
            if key in self.stat:
                self.stat[key] += 1
            else:
                self.stat[key] = 1

    def give_stat(self):
        with open(file='stat.txt', mode='w+', encoding='utf8') as file:
            for key, item in self.stat.items():
                file.write(f'{key}]  {item}''\n')

    def change_groupby(self):
        pass

    def run(self):
        self.change_groupby()
        self.collect()
        self.give_stat()


class HoursParser(Parser):

    def change_groupby(self):
        self.right = 14


logs = HoursParser(filename='events.txt')
logs.run()
