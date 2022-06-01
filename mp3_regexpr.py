# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp3_regexpr.py

import re

class RegExpr:
    def __init__(self):
        self._expr = None
        self._match = None
    
    def input_expression(self, expression):
        self._expr = expression
    
    def get_match(self):
        return self._match

    def auto(self, expression):
        self.input_expression(expression)

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
    expr = RegExpr
    Interpreter()


if __name__ == "__main__":
    main()