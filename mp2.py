# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp2.py

import re

primitive_types = ["int", "char", "float", "double"]
reserved_names = ["void"]
allowed_var_names = ["_"]
for _ in range(10):
    allowed_var_names.append(str(_))
for _ in range(26):
    allowed_var_names.append(chr(65+_))
    allowed_var_names.append(chr(97+_))
reserved_names += primitive_types

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
        while self._instructions:
            current_syntax = self._instructions.pop() 
            current_syntax = current_syntax.rstrip() # removes newlines
                
            if self.check_type(current_syntax) == "FUNCTION":
                if self.validate_function(current_syntax):
                    self._results.append("VALID FUNCTION DECLARATION")
                else:
                    self._results.append("INVALID FUNCTION DECLARATION")

            elif self.check_type(current_syntax) == "VARIABLE":
                if self.validate_variable(current_syntax):
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

    def validate_variable(self, current_syntax):
        if current_syntax[-1] != ';':
            return False
        cs = current_syntax.replace(';', '')
        cs = cs.split(',')
        for _ in range(len(cs)):
            cs[_] = cs[_].split()
        
        validator = VariableSyntaxParser(cs)
        return(validator.result())
    
    def validate_function(self, current_syntax):
        if current_syntax[-1] != ';':
            return False
        cs = current_syntax.replace(';', '')
        validator = FunctionSyntaxParser(cs)
        
        return(validator.result())


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

class FunctionSyntaxParser:
    def __init__(self, syntax = list(), *args):
        self._syntax = syntax
        self._isValid = True

        self._isValid = self.check_type()
        print()

    def check_type(self):
        ptype = re.search("\w+", self._syntax)[0] 
        if ptype not in primitive_types:
            return False

        syntax = "".join(self._syntax)
        syntax = syntax.replace(ptype+" ", '')
        print(syntax)

        return True


    def result(self):
        return self._isValid

    def print_args(self):
        for _ in self._syntax:
            print(_)

class VariableSyntaxParser:
    def __init__(self, syntax = list(), *args):
        self._syntax = syntax
        self._isValid = True

        self._isValid = self.check_type()
        while self._syntax:
            self._isValid = self.check_variable()
            self._syntax.pop(0)
        
    def check_type(self):
        # if self._syntax[0].count("=") > 1:
        #     return False

        # if self._syntax[0].count("=") == 1:
        #     temp = self._syntax[0].replace(" ", '')
        #     print(temp)

        if self._syntax[0][0] not in reserved_names:
            return False
        self._syntax[0].pop(0)

    def check_variable(self):
        for i in range(len(self._syntax)):
            for word in self._syntax[i]:
                if word in reserved_names:
                    return False
            return self.var_naming(self._syntax[i][0])


    def var_naming(self, variable):
        variable = list(variable)
        nums = []
        for _ in range(9):
            nums.append(str(_))
        if variable[0] in nums:
            return False

        for _ in variable:
            if _ not in allowed_var_names:
                if _ == "=":
                    break
                return False

        return True
    
    def result(self):
        return self._isValid

    def print_args(self):
        for _ in self._syntax:
            print(_)



def main():
    validate = ProcessInterpreter("mpa2.in")

    
    

if __name__ == '__main__':
    main()