primitive_types = ["int", "char", "float", "double", "void"]


class FileHandler:
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
        return self._lines[line] if abs(line) < len(self._lines) else None

    def _get_size(self):
        return len(self._lines)

    def get_me(self):
        return self._lines



class ProcessInterpreter:
    def __init__(self, filename):
        self._file = FileHandler(filename)
        self._file.start_reading()
        if self._file._get_size() == 0:
            raise ValueError("File length is 0.")

        self._instructions = self._file.get_me()
        self._instructions.reverse()
        self._cases = self._instructions.pop()
        self._results = list()

        self.validate()


    def validate(self):
        while len(self._instructions) != 0:
            current_syntax = self._instructions.pop()

            if not self.check_init(current_syntax):
              self._results.append("INVALID SYNTAX")
                
            if self.check_type(current_syntax) == "FUNCTION":
                print("function")
            elif self.check_type(current_syntax) == "VARIABLE":
                print("variable")



        print(self._results)

    def check_init(self, current_syntax):
        if ';' in current_syntax:
            return True
        else:
            return False
    
    def check_type(self, current_syntax):
        if '(' in current_syntax or ')' in current_syntax:
            return "FUNCTION"
        else:
            return "VARIABLE"

    def check_variable(self, current_syntax):
        pass
        """check variable"""



def main():
    validate = ProcessInterpreter("mpa2.in")
    
    

if __name__ == '__main__':
    main()