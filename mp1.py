# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.py

"""
    Test Cases: Amount of times creating new two sets.
"""

#from abc import ABC, abstractmethod
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


class _Set:
    def __init__(self):
        self._set_type = None
        self._set_list = {}

    def _list(self) -> set:
        return self._set_list

    def _print(self):
        for item in self._set_list:
            print(item)

    def insert(self, value):
        pass
    
    def remove(self, value):
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

class _SetTypeCreator:
    """
        This class returns the type of set
    """
    def __init__(self, set_type: int) -> _Set:
        self._types = {
                        1: _SetInteger
                        
                        }
        return self._types[set_type]

class _SetInteger(_Set):
    def __init__(self):
        self._set_type = int
        self._set_list = {}

class Interface:
    """
        This class should be handling how we navigate through the sets. By creating, modifying,
        removing items from a set. An API perhaps?
    """

    def __init__(self, tests: int, file):
        """
            __init__ is step 0 or the initialization
            We load the inititials:
                test_cases      : Amount of test cases
                test_file       : file input of test cases
                set_case        : ?
        """
        self._test_cases = tests
        self._test_file = InputFileHandler(file)
        self._test_file.start_reading()

        # setting default none values
        self._set1 = None
        self._set2 = None

    def step_1(self, value):
        """
            Get the type of set for the elements:
                1               : int
                2               : double
                3               : char
                4               : string
                5               : set
                6               : object
        """
        self._set1 = _Set(value)
        self._set2 = _Set(value)
    
    def step_2(self, value):
        pass
        
        

def main():
    #new_test = Interface(input("test_cases: "), "mpa1.in")
    _SetInteger()
    


if __name__ == '__main__':
    main()
