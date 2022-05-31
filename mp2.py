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

expected_chars = [';', ',', '=', '(', ' ']

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




class DeterministicFiniteAutomaton:
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
            self._cases = int(input("Test cases: "))
            for i in range(self._cases):
                self._instructions.append(input("Instruction: "))

        while self._instructions:
            self.syntax = list(self._instructions.pop(0))
            self.syntax2 = ''.join([s for s in self.syntax]) ####
            if '(' in self.syntax or ')' in self.syntax:
                self._type = "FUNCTION"
            else:
                self._type = "VARIABLE"


            valid = True
            while valid:
                valid = self.state_type()
                valid = self.state_space(1)
                valid = self.state_declaration(2)
                valid = self.state_expectations(3)

                valid = True
                self.state_final(valid)
                break
            

    
    def state_type(self):
        word = ""

        while self.syntax:
            c = self.syntax.pop(0)
            if c == ' ':
                self.syntax.insert(0, c)
                break
            word += c
        
        if word not in primitive_types:
            if self._type == "VARIABLE":
                return False
            else:
                if word != "void":
                    return False
        return True


    def state_space(self, state):
        word = ""
        if state == 1:
            if len(self.syntax) == 0:
                return False

            while self.syntax:
                c = self.syntax.pop(0)
                if c != ' ':
                    self.syntax.insert(0, c)
                    break
                word += c
            

    def state_declaration(self, state):
        word = ""
        if state == 2:
            if len(self.syntax) == 0:
                return False
            
            self.syntax = ''.join([s for s in self.syntax])
            word = re.search("([^\s|,|;|=|(]+)", self.syntax)[0]
            self.syntax = self.syntax.replace(word, '', 1)

            for c in word:
                if c not in allowed_var_names:
                    return False
            if word[0] in str(list(range(9))):
                return False
            self.syntax = list(self.syntax)

    def state_expectations(self, state):
        if len(self.syntax) == 0:
            return False
        else:
            if state == 3:
                # [';', ' ']
                if self.syntax[0] == ';':
                    self.state_semicolon(3)

    
    def state_semicolon(self, state):
        if state == 3:
            if len(self.syntax) == 1:
                return True
            if len(self.syntax) > 1:
                pass


    def state_final(self, valid):
        if valid == False:
            if self._type == "FUNCTION":
                print(f"INVALID FUNCTION DECLARATION: {self.syntax2}")
                #print("INVALID FUNCTION DECLARATION")

            if self._type == "VARIABLE":
                print(f"INVALID VARIABLE DECLARATION: {self.syntax2}")
                #print("INVALID VARIABLE DECLARATION")
        if valid == True:
            if self._type == "FUNCTION":
                print(f"VALID FUNCTION DECLARATION: {self.syntax2}")
                #print("VALID FUNCTION DECLARATION")

            if self._type == "VARIABLE":
                print(f"VALID VARIABLE DECLARATION: {self.syntax2}")
                #print("VALID VARIABLE DECLARATION")


def main():
    #parse = DeterministicFiniteAutomaton()
    parse = DeterministicFiniteAutomaton("mpa2.in")

    
    

if __name__ == '__main__':
    main()