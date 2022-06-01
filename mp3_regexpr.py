# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp3_regexpr.py

import re
from threading import current_thread

class RegExpr:
    def __init__(self, case):
        self._match = list()
        self._orig_expr = case[0].replace(' ', '')
        self._strings = case[1]
        self._expr = [self._orig_expr]
    
    def test_a_string(self):
        for i in range(len(self._strings)):
            valid = re.search(f"{self._expr}", self._strings[i])
            if self._strings[i] == 'e':
                if '*' in self._expr:
                    self._match.append(True)
                else:
                    self._match.append(False)
            else:
                if valid == None:
                    self._match.append(False)
                else:
                    if valid[0] == self._strings[i]:
                        self._match.append(True)
                    else:
                        self._match.append(False)

    def get_match(self):
        return self._match

    def build_regex(self) -> list():
        print("Original:", self._expr)
        current_regex = self._expr.pop(0)
        print(current_regex, self._expr)

        ors = re.findall("\(([^()]+)\)", current_regex)
        current_regex =  current_regex.replace("("+ors[0]+")", '')
        current_regex =  current_regex.replace("("+ors[1]+")", '')
        print(ors, current_regex)
        




    def auto(self):
        self.test_a_string()

        return self.get_match()


def Interpreter() -> dict():
    data = dict()

    test_cases = input()
    
    for tc in range(int(test_cases)):
        reg_expr = input()
        num = input()
        temp_list = []
        
        for _ in range(int(num)):
            temp_list.append(input())
        data[tc] = [reg_expr, temp_list]

    return data


def main():
    #data = Interpreter()
    data = {
    0: ["a*b*",   ["aaabbbbbb", "aaaaaa", "bbbbbaaaaa"]],
    1: ["a + b", ["a", "b"]],
    2: ["(ab)*(aa + bb)",  ["aa", "e", "abababbb", "ababababaaaaab", "aaaaaabbbbbb", "bbbbbbababab"]]
}
  
    for i in range(len(data)):
        expr = RegExpr(data[i])
        results = expr.auto()
        
        for i in range(len(results)):
            if results[i] == True:
                print("yes")
            else:
                print("no")
        expr.auto()

def test():
    data = {
    0: ["a*((b+e)a+a(b+e))a*",   ["aaabbbbbb", "aaaaaa", "bbbbbaaaaa"]]
}
    expr = RegExpr(data[0])
    expr.build_regex()


if __name__ == "__main__":
    #main()
    test()