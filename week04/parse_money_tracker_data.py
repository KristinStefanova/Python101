class Parser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = []

    def read_file(self):
        with open(self.file_name, 'r') as f:
            return f.read()

    def make_rows(self):
        self.file = self.read_file().split('\n')

    def save_file(self):
        with open(self.file_name, 'w') as f:
            f.write("\n".join(self.file))


def main():
    par = Parser("money_tracker.txt")
    par.make_rows()

    print(par.file)


if __name__ == '__main__':
    main()
