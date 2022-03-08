class Set_mp:
    def __init__(self, set_data: {}):
        self._set_data = set_data
        print(len(self._set_data))

    def _list(self) -> {}:
        return self._set_data

    def _print(self):
        for item in self._set_data:
            print(item)

    def insert(self, set_data: set):
        pass

    def remove(self):
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


def main():
    num = Set_mp({1,2,34,42,212})
    num.insert({42})
    print(num._list())


if __name__ == '__main__':
    main()
