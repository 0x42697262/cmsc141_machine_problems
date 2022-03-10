class InputFileHandler:
    def __init__(self, filename):
        self._filename = filename
        self._lines = []

    def start_reading(self):
        with open(self._filename, "r") as file:
            for line in file.readlines():
                self._lines.append(line)

    def _print(self):
        for line in self._lines:
            print(line)
    
    def _get_line(self, line:int):
        return self._lines[line-1] if abs(line-1) < len(self._lines) else None


class Interface:
    def __init__(self, tests: int):
        self._tests = tests
class Set_mp:
    def __init__(self, set_data: set):
        self._set_data = set_data
        print(len(self._set_data))

    def _list(self) -> set:
        return self._set_data

    def _print(self):
        for item in self._set_data:
            print(item)

    def insert(self, item):
        pass

    def remove(self, item):
        pass

    def subset(self):
        pass

    def union(self):
        pass

    def intersection(self):
        pass

    def difference(self):
        pass

    def power_set(self):
        pass

def main():
    file = InputFileHandler("mpa1.in")
    file.start_reading()


if __name__ == '__main__':
    main()
