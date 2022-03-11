# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1.py

"""
    Test Cases: Amount of times creating new two sets.
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


class _Set:
    def _list(self) -> set:
        return self._set_list

    def _print(self):
        for item in self._set_list:
            print(item)

    def _get_type(self):
        return self._set_type

    # def _init_type(self, value):
    #     types = {
    #         1: int,
    #         2: float,
    #         3: str,
    #         4: str,
    #         5: set,
    #         6: object
    #     }
    #     return types[value]

    def insert(self, value):
        if not isinstance(value, self._set_type):
            raise TypeError(f"set item is of only type {self._set_type}")
        self._set_list.add(value)
    
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
        This function returns the type of set: (int, double, char, string, set, object)
    """
    def init_set(value: int, value2: int) -> _Set:
        stypes = {
                        1: _SetInteger,
                        2: _SetDouble,
                        3: _SetChar,
                        4: _SetString,
                        5: _SetSets,
                        6: _SetObject                        
                        }
        return stypes[value]()

class _SetInteger(_Set):
    def __init__(self):
        self._set_type = int
        self._set_list = set()

class _SetDouble(_Set):
    def __init__(self):
        self._set_type = float
        self._set_list = set()

class _SetChar(_Set):
    def __init__(self):
        self._set_type = str
        self._set_list = set()
    
    def insert(self, value: str):
        if not isinstance(value, self._set_type):
            raise TypeError(f"set item is of only type {self._set_type}")
        self._set_list.add(value[0])

class _SetString(_Set):
    def __init__(self):
        self._set_type = str
        self._set_list = set()

class _SetSets(_Set):
    def __init__(self):
        self._set_type = set
        self._set_list = set()
    

    def insert(self, set_value: set):
        if not isinstance(set_value, self._set_type):
            raise TypeError(f"set item is of only type {self._set_type}")
        self._set_list.update(set_value)


class _SetObject(_Set):
    def __init__(self):
        self._set_type = object
        self._set_list = set()

# ----------------------------------------------------------------- #
class Interface:
    """
        This class should be handling how we navigate through the sets. By creating, modifying,
        removing items from a set. An API perhaps?

        Flow:
            1) Initialize the sets - test cases
            2) Choose the set type for the each test case - execute _SetTypeCreator($type$)
                -> must strictly only use the specified set type for the created set
            3) Fill the two sets with data (based on the $type$ of set you specified.)
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



    def step_1(self):
        """
            Get the type of set for the elements:
                1               : int
                2               : double
                3               : char
                4               : string
                5               : set
                6               : object
        """
        value = list(map(str, input().split()))
        value.append(None)
        value[0] = int(value[0])

        self._set1 = _SetTypeCreator.init_set(value[0], value[1])
        self._set2 = _SetTypeCreator.init_set(value[0], value[1])

        

    def step_2(self):
        for item in list(map(self._set1._get_type(), input("set_items1: ").split())):
            self._set1.insert(item)
        for item in list(map(self._set2._get_type(), input("set_items2: ").split())):
            self._set2.insert(item)

        

        print(self._set1._list())
        print(self._set2._list())
        

def main():
    new_test = Interface(input("test_cases: "), "mpa1.in")
    new_test.step_1()
    new_test.step_2()
    
    


if __name__ == '__main__':
    main()
