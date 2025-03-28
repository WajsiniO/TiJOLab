class Zbiory:
    def __init__(self, list_, repeat_number):
        self.list_ = list_ if list_ is not None else []
        self.repeat_number = repeat_number

    def list_checkers(self):
        # Znajdowanie elementów powtarzających się dokładnie (repeat_number) razy
        counted = {elem: self.list_.count(elem) for elem in set(self.list_)}
        repeated_elems = [elem for elem, count in counted.items() if count == self.repeat_number]

        return repeated_elems

    def printer(self):
        print(self.list_checkers())


def main():
    test_cases = [
        ([2, 2, 2, 3, 1, 1, 4, 5], 2),
        ([1, 1, 2, 2, 2, 4, 5, 5, 1], 3),
        ([1, 2, 2, 2, 3, 4, 5, 5, 1], 2),
        (None, 1),
        ([1,2,3], None),
        (None, None),
        ([1,1,2,2,2,3,4,5], 7)
    ]

    for list_, repeat_number in test_cases:
        zbior = Zbiory(list_, repeat_number)
        zbior.printer()


if __name__ == "__main__":
    main()
