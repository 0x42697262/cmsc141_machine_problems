primitive_types = ["int", "char", "float", "double"]


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
            current_syntax = current_syntax.rstrip() # removes newlines
                
            if self.check_type(current_syntax) == "FUNCTION":
                self._results.append("FUNCTION DECLARATION")

            elif self.check_type(current_syntax) == "VARIABLE":
                if self.check_variable(current_syntax):
                    self._results.append("VALID VARIABLE DECLARATION")
                else:
                    self._results.append("INVALID VARIABLE DECLARATION")



        for _ in self._results:
            print(_)

    def check_type(self, current_syntax):
        if '(' in current_syntax or ')' in current_syntax:
            return "FUNCTION"
        else:
            return "VARIABLE"

    def check_variable(self, current_syntax):
        if current_syntax[-1] != ';':
            return False

        cs_s = current_syntax.replace(';', '')
        cs_s = cs_s.split(',')

        temp_cs = cs_s.pop(0).split()
        if temp_cs[0] in primitive_types:
            for i in range(1, len(temp_cs)):
                if temp_cs[i] in primitive_types:
                    return False
            temp_cs.pop(0)
            ns = ' '.join(map(str, temp_cs)).replace(" ", '')

        else:
            return False
        print(temp_cs)
        print(ns)

        for i in range(len(cs_s)):
            temp_cs = cs_s.pop(0).split()
            for pt in primitive_types:
                if pt in temp_cs:
                    return False
        
        #print(ns)
        
        
            """
            this is a fail.
            """
        



        return True



def main():
    validate = ProcessInterpreter("mpa2.in")
    
    

if __name__ == '__main__':
    main()