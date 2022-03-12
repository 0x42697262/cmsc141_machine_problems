
# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1_v2.py

"""
    NO MORE CODE EXPLANATIONS!!!
    welcome to 12:14 UTC+8 coding. HAVE FUN!
"""


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





def main():
    print('hi')    
    


if __name__ == '__main__':
    main()
