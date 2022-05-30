# source: https://github.com/KrulYuno/cmsc141_machine_problems/blob/master/mp1_v2.py

"""
12/05/22 - I forgot what i was doing here... I should've documented my code... 
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


class SetDouble(Set):
    def insert(self, value):
        if isinstance(value, self._set_type):
            value = round(value, 2)
            self._set_list[str(value)] = value

class SetChar(Set):
    def insert(self, value):
        if isinstance(value, self._set_type):
            self._set_list[str(value[0])] = value[0]



class Interface:
    def __init__(self, filename: str):
        self._ㄋ = InputFileHandler(filename)
        self._ㄋ.start_reading()
        self._stack = list()

        self._stack_generator()
        self.process()

    def _stack_generator(self):
        for i in range(self._ㄋ._get_size()):
            c_line = self._ㄋ._get_line(i)
            line_list = list(map(str, c_line.split()))

            if len(line_list) == 1:
                self._stack.append(line_list[0])
            else:
                self._stack.append(line_list)

        self._stack = self._stack[::-1]

    def process(self):
        data = {
            'test_cases': int(self._stack.pop()),
            'case_id': 0, 
            'operations': 0, 
            'new_case': True
        }

        set_settings = {
            "set1": None,
            "set2": None
        }

        set_types = {
            1: int,
            2: float,
            3: str,
            4: str,
            5: str,
            6: object
        }

        set_class = {
            1: Set,
            2: SetDouble,
            3: SetChar,
            4: Set,
            5: Set,
            6: Set
        }

        while data['case_id'] < data['test_cases']:
            if data['new_case'] == True:
                thingy = self._stack.pop()

                s_type = int(thingy[0])
                set_settings['set1'] = set_class[s_type](set_types[s_type])
                set_settings['set2'] = set_class[s_type](set_types[s_type])

                for item in self._stack.pop():
                    set_settings['set1'].insert(set_types[s_type](item))

                for item in self._stack.pop():
                    set_settings['set2'].insert(set_types[s_type](item))
            
                data['operations'] = int(self._stack.pop())
                data['new_case'] = False

            for _ in range(data['operations']):
                self._stack.pop()

            
            
            data['new_case'] = True
            data['operations'] = 0
            data['case_id'] += 1


    def operate(self):
        pass


def main():
    #ㄏㄢㄋㄚㄏ = Interface("mpa1.in")    
    ㄏㄢㄋㄚㄏ = Interface("mp1_test.in")
    


if __name__ == '__main__':
    main()

