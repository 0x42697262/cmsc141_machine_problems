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

expected_chars = [';', ',', '=', '(', ')']

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



class DFA:
    def __init__(self, declaration_type, syntax):
        self._syntax = syntax
        self._type = declaration_type
        self._results = None

        self.var_names = []
        self.func_names = []
        self.var_type = None


        self.add_space()
        self.state_type()


    def add_space(self):
        for _ in range(len(expected_chars)):
            self._syntax = self._syntax.replace(expected_chars[_], f" {expected_chars[_]} ")
        self._syntax = self._syntax.split()

    def transitions(self, state, expectation):
        if expectation == -1:
            self.state_invalid()
            return False

        if state == 0:  # type
            if expectation == 0:
                self.state_variable()

        if state == 1:  # variable
            if expectation == ',':
                self.state_variable()
            elif expectation == ';':
                self.state_semicolon()
            elif expectation == '=':
                self.state_equal()
        
        if state == 2:  # semicolon
            if expectation == 0:
                self.state_valid()
            elif expectation == 1:
                self.state_semicolon()
            elif expectation == 2:
                self.state_type()
            else:
                self.state_invalid()

        if state == 3:  # equal
            if expectation == ',':
                self.state_variable()
            elif expectation == ';':
                self.state_semicolon()
            else:
                self.state_invalid()

        if state == 4:
            if expectation == '(':
                self.state_type_func()
            else:
                self.state_invalid()
        
        if state == 4.1:    # types
            if expectation == ',':
                self.state_type_func()
            elif expectation == ')':
                self.state_sc_func()
            else:
                self.state_var_func()
        
        if state == 4.2:    # var
            if expectation == ',':
                self.state_type_func()
            elif expectation == '=':
                self.state_equal_func()
            elif expectation == ')':
                self.state_sc_func()
            else:
                self.state_invalid()

        if state == 4.3:    # equal
            if expectation == ',':
                self.state_type_func()
            elif expectation == ')':
                self.state_sc_func()
            else:
                self.state_invalid()
        
        if state == 5:
            if expectation == ';':
                pass
            else:
                self.state_type()

    
    def state_type(self):
        self.var_names = []
        self.func_names = []
        self.var_type = None

        word = self._syntax.pop(0) # empty list index error
        if word[0] == ';':
            self.transitions(2, 2)
            return True


        if word not in primitive_types:
            if self._type == "VARIABLE":
                self.transitions(0, -1)
                return False
            else:
                if word != "void":
                    self.transitions(0, -1)
                    return False
        
        self.var_type = word
        self.transitions(0, 0)
    
    def state_variable(self):
        if len(self._syntax):
            word = self._syntax.pop(0)

            if word[0] in str(list(range(9))):
                self.transitions(1, -1)
                return False

            if word in primitive_types or word in reserved_names or word in self.var_names:
                self.transitions(1, -1)
                return False

            for c in word:
                if c not in allowed_var_names:
                    self.transitions(1, -1)
                    return False

            
        else:
            self.transitions(1, -1)
            return False

        if self._type == "FUNCTION":
            self.func_names.insert(0, word)
        if self._type == "VARIABLE":
            self.var_names.insert(0, word)

        if len(self._syntax):
            if self._syntax[0] in [';', ',', '=']:
                self.transitions(1, self._syntax.pop(0))
            elif self._syntax[0] == '(' and self._type == "FUNCTION":
                self.transitions(4, self._syntax.pop(0))
            else:
                self.transitions(1, -1)
                return False
        else:
            self.transitions(1, -1)
            return False

        
    def state_semicolon(self):
        if len(self._syntax):
            word = self._syntax.pop(0)
            if word == ';':
                self.transitions(2, 1)

            else:
                self._syntax.insert(0, word)
                self.transitions(2, 2)            
           
          
        else:
            self.transitions(2, 0)
            return True
    
    def state_equal(self):
        if len(self._syntax):
            word = self._syntax.pop(0)
            if self.var_type == "int" or self.var_type == "double" or self.var_type == "float" :
                valid = re.search("[+-]?([0-9]*[.])?[0-9]+", word)
                if valid != None: 
                    valid = valid[0]

                if word == valid or word in self.var_names:
                    if len(self._syntax):
                        self.transitions(3, self._syntax.pop(0))
                    else:
                        self.transitions(3, -1)
                        return False
                elif word.count("'") == 2  or word in self.var_names:
                    self.transitions(3, self._syntax.pop(0))

                else:
                    self.transitions(3, -1)
                    return False
            elif self.var_type == "char":
                valid = re.search("[+-]?([0-9]*[.])?[0-9]+", word)
                if valid != None: 
                    valid = valid[0]

                if word.count("'") == 2  or word in self.var_names:
                    self.transitions(3, self._syntax.pop(0))
                
                elif word == valid or word in self.var_names:
                    if len(self._syntax):
                        self.transitions(3, self._syntax.pop(0))
                    else:
                        self.transitions(3, -1)
                        return False
                else:
                    self.transitions(3, -1)
                    return False

        else:
            self.transitions(3, -1)
            return False

    def state_type_func(self):
        if len(self._syntax):
            word = self._syntax.pop(0)

            if word not in reserved_names:
                if word == ')':
                    self.transitions(4.1, word)
                    return True
                self.transitions(4.1, -1)
                return False

            if len(self._syntax):
                t = self._syntax.pop(0)
                if t == ',' or t == ')' or t == '(':
                    pass
                else:
                    self._syntax.insert(0, t)
            
                self.transitions(4.1, t)
                return True
        
        self.transitions(4.1, -1)
        return False

    def state_var_func(self):
        if len(self._syntax):
            vars = []
            word = self._syntax.pop(0)
            if word[0] in str(list(range(9))):
                self.transitions(4.2, -1)
                return False

            if word in primitive_types or word in reserved_names or word in self.var_names:
                self.transitions(4.2, -1)
                return False

            for c in word:
                if c not in allowed_var_names:
                    self.transitions(4.2, -1)
                    return False

            vars.insert(0, word)

            if len(self._syntax):
                self.transitions(4.2, self._syntax.pop(0))
            else:
                self.transitions(4.2, -1)
                return False    

            return True
        

        self.transitions(4.2, -1)
        return False

    def state_sc_func(self):
        if len(self._syntax):
            word = self._syntax.pop(0)
            if word == ';':
                self.sc_checker()
                if len(self._syntax) == 0:
                    self.transitions(2, 0)
                else:
                    self.transitions(5, 0)            
                return True
            elif word == ',':
                self.transitions(0, 0)
                return True


        self.transitions(5, -1)
        return False

    def sc_checker(self):
        while self._syntax:
            word = self._syntax.pop(0)
            if word != ';':
                self._syntax.insert(0, word)
                break

# int function(int)int a = 10;
# int area(int a int b);
# int perimeter(int,int abc_cbn)
    def state_equal_func(self):
        if len(self._syntax):
            word = self._syntax.pop(0)
            if self.var_type == "int" or self.var_type == "double" or self.var_type == "float" :
                valid = re.search("[+-]?([0-9]*[.])?[0-9]+", word)
                if valid != None: 
                    valid = valid[0]

                if word == valid or word in self.var_names:
                    if len(self._syntax):
                        self.transitions(4.3, self._syntax.pop(0))
                    else:
                        self.transitions(4.3, -1)
                        return False
                elif word.count("'") == 2  or word in self.var_names:
                    self.transitions(4.3, self._syntax.pop(0))

                else:
                    self.transitions(3, -1)
                    return False
            elif self.var_type == "char":
                valid = re.search("[+-]?([0-9]*[.])?[0-9]+", word)
                if valid != None: 
                    valid = valid[0]

                if word.count("'") == 2  or word in self.var_names:
                    self.transitions(3, self._syntax.pop(0))
                
                elif word == valid or word in self.var_names:
                    if len(self._syntax):
                        self.transitions(4.3, self._syntax.pop(0))
                    else:
                        self.transitions(4.3, -1)
                        return False
                else:
                    self.transitions(4.3, -1)
                    return False

        else:
            self.transitions(4.3, -1)
            return False

        
    def state_valid(self):
        self._results = True

    def state_invalid(self):
        self._results = False        

    def get_result(self):
        return self._results



class CParser:
    def __init__(self, filename = None):
        self._type = None
        self._instructions = list()
        self.cases = None
        self.syntax = None

        self.syntax2 = None ####

        if filename != None:
            self._file = FileHandler(filename)
            self._file.start_reading()
            if self._file._get_size() == 0:
                raise ValueError("File length is 0.")

            self._instructions = self._file.get_me()
            self._cases = self._instructions.pop(0)

            for _ in range(len(self._instructions)):
                self._instructions[_] = self._instructions[_].rstrip()
        else:
            #self._cases = int(input("Test cases: "))
            self._cases = int(input())
            for i in range(self._cases):
                self._instructions.append(input())
                #self._instructions.append(input("Instruction: "))

        while self._instructions:
            self.syntax = self._instructions.pop(0)
            if '(' in self.syntax or ')' in self.syntax:
                self._type = "FUNCTION"
            else:
                self._type = "VARIABLE"
            parser = DFA(self._type, self.syntax)
            #print(parser.get_result(), " | ", self.syntax)
            self.print_result(parser.get_result())
    
    def print_result(self, valid):
        if valid == False:
            if self._type == "FUNCTION":
                print("INVALID FUNCTION DECLARATION")

            if self._type == "VARIABLE":
                print("INVALID VARIABLE DECLARATION")
        if valid == True:
            if self._type == "FUNCTION":
                print("VALID FUNCTION DECLARATION")

            if self._type == "VARIABLE":
                print("VALID VARIABLE DECLARATION")
        

        


def main():
    parse = CParser()
    #parse = CParser("mpa2.in")

    
    

if __name__ == '__main__':
    main()