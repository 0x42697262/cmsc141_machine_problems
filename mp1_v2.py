
# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1_v2.py

"""
    NO MORE CODE EXPLANATIONS!!! everything will be built around dictionaires and strings A LOT OF STRINGS.
    welcome to 12:14 UTC+8 coding. HAVE FUN!

    03:38 - i am dying help me. i still haven't set the other types.
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
        return self._lines[line] if abs(line) < len(self._lines) else None

    def _get_size(self):
        return len(self._lines)

    def get_me(self):
        return self._lines



class Set:
    def __init__(self, s_type):
        self._set_type = s_type
        self._set_list = dict()

    def _print(self) -> None:
        for item in self._set_list:
            print(item)
    
    def _get_type(self):
        return self._set_type
    
    def get_list(self) -> dict:
        return self._set_list

    def _feed(self, o_set: set):
        if self._set_type == o_set._get_type():
            self._set_list = o_set.get_list().copy()

    def insert(self, value):
        if isinstance(value, self._set_type):
            self._set_list[str(value)] = value

    def remove(self, value):
        value = str(value)
        if value in self._set_list:
            self._set_list.pop(value)

    def subset(self, o_set: set) -> set:
        for value in self._set_list:
            if value not in o_set:
                return False
        return True
    
    def union(self, o_set: set) -> set:
        if self._set_type == o_set._get_type():
            new_set = Set(self._set_type)
            new_set._feed(self)

            for values in o_set.get_list().values():
                new_set.insert(values)

            return new_set

    def intersection(self, o_set: set) -> set:
        if self._set_type == o_set._get_type():
            new_set = Set(self._set_type)

            for values in self._set_list.values():
                if values in o_set.get_list().values():
                    new_set.insert(values)

            return new_set

    def difference(self, o_set: set) -> set:
        if self._set_type == o_set._get_type():
            new_set = Set(self._set_type)

            for values in self._set_list.values():
                if values not in o_set.get_list().values():
                    new_set.insert(values)

            return new_set

    def power_set(self, o_set: set) -> set:
        pass


class Interface:
    def __init__(self, filename: str):
        self._ㄋ = InputFileHandler(filename)
        self._ㄋ.start_reading()
        self._test_cases = None
        self._case_id = 0
        self._stack = list()

        self._index_stack_cases = list()
        self._index_stack_operations = list()

        self._set1 = None
        self._set2 = None
        self._type = None

        self._current_case = 0 

        self._stack_generator()
        self._create_stack_flow()

    def _create_sets(self):
        self._set1 = Set
        self._set2 = Set

    def _stack_generator(self):
        for i in range(self._ㄋ._get_size()):
            c_line = self._ㄋ._get_line(i)
            line_list = list(map(str, c_line.split()))

            if len(line_list) == 1:
                self._stack.append(line_list[0])
            else:
                self._stack.append(line_list)
        self._stack = self._stack[::-1]
        self._test_cases = self._stack.pop()

    def _create_stack_flow(self):
        print(self._test_cases)
        

def main():
    #ㄏㄢㄋㄚㄏ = Interface("mpa1.in")    
    ㄏㄢㄋㄚㄏ = Interface("mp1_test.in")    
    print()
    X = Set(int)
    Y = Set(int)

    X.insert(1)
    X.insert(2)
    X.insert(3)

    Y.insert(3)
    Y.insert(4)
    Y.insert(5)

    print(X.intersection(Y).get_list())
    print(X.union(Y).get_list())
    print(X.difference(Y).get_list())
    #print(X.power_set(Y).get_list())


if __name__ == '__main__':
    main()

