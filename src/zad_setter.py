from audioop import error


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        # Problem!
        if new_age < 0 or new_age % 1 != 0 or new_age > 130:
            raise error("Niepoprawne dane")
            return
        self._age = new_age

def main():
    user = User("Jan", 30)
    print(f"Poczatkowy wiek: {user.get_age()}")

    user.set_age(-5)
    print(f"Wiek po ustawieniu nieprawidlowej wartosci: {user.get_age()}")

    user.set_age(200)
    print(f"Wiek po ustawieniu absurdalnie duzej wartosci: {user.get_age()}")

    user.set_age(35.5)
    print(f"Wiek po ustawieniu absurdalnie duzej wartosci: {user.get_age()}")

if __name__ == '__main__':
    main()

