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

nums = ['=', ';', ',', '(']
for _ in range(9):
    nums.append(str(_))

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

        self.syn = None ### delete

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
        
        self.state_init()


    def state_init(self):
        while self._instructions:
            self.syn = self._instructions.pop(0)
            self.state_type(self.syn)

    def state_type(self, syntax):
        if '(' in syntax or ')' in syntax:
            self._type = "FUNCTION"
        else:
            self._type = "VARIABLE"

        ptype = re.search("\w+", syntax)[0]
        if ptype not in primitive_types:
            if self._type == "VARIABLE":
                self.state_invalid()
                return False
            else:
                if ptype != "void":
                    self.state_invalid()
                    return False
        
        syntax = syntax.replace(ptype, '')
        self.state_space(syntax)

    def state_space(self, syntax):
        word = re.search("\s+", syntax)[0]
        if syntax[:len(word)] != word:
            self.state_invalid()
            return False
        
        syntax = syntax.replace(word, '', 1)
        self.state_declaration(syntax)

    def state_declaration(self, syntax):
        if len(syntax) <= 1:
            temp_syntax = syntax
        else:
            temp_syntax = syntax[:-1]

        
        
        if temp_syntax[0] in nums:
            self.state_invalid()
            return False

        word = re.search("([^\s|,|;|=|(]+)", temp_syntax)[0]
        for c in word:
            if c not in allowed_var_names:
                self.state_invalid()
                return False
        syntax = syntax.replace(word, '', 1)
        
        self.state_branches(syntax)
        
        
    def state_space_branch(self, syntax):
        # Expecting a ' ', variable, '(', ')', or ';'
        word = re.search("\s+", syntax)[0]
        if syntax[:len(word)] != word:
            self.state_invalid()
            return False
        
        syntax = syntax.replace(word, '', 1)

        #print(syntax)
        # do some if else for every branches please
        self.state_branches(syntax)

    def state_branches(self, syntax):
        if syntax[0] == ';':
            syntax = syntax.replace(';', '', 1)
            if len(syntax) == 0:
                self.state_valid()
                return True
            else:
                self.state_branches(syntax)
        if syntax[0] == ' ':
            self.state_space_branch(syntax)



    def state_invalid(self):
        if self._type == "FUNCTION":
            print(f"INVALID FUNCTION DECLARATION: {self.syn}")
            #print("INVALID FUNCTION DECLARATION")

        if self._type == "VARIABLE":
            print(f"INVALID VARIABLE DECLARATION: {self.syn}")
            #print("INVALID VARIABLE DECLARATION")
    
    def state_valid(self):
        if self._type == "FUNCTION":
            print(f"VALID FUNCTION DECLARATION: {self.syn}")
            #print("VALID FUNCTION DECLARATION")

        if self._type == "VARIABLE":
            print(f"VALID VARIABLE DECLARATION: {self.syn}")
            #print("VALID VARIABLE DECLARATION")



def main():
    #parse = DeterministicFiniteAutomaton()
    parse = DeterministicFiniteAutomaton("mpa2.in")

    
    

if __name__ == '__main__':
    main()