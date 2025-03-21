from src.User import User
class ATM:

    def __init__(self, pin: int, balance: float):
        self.pin = pin
        self.balance = balance
        self.user = User(pin, balance)


    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :return: Saldo konta uĹźytkownika.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if self.user.pin == pin:
            return self.user.balance
        else:
            raise ValueError("Invalid pin")

    def deposit(self, pin: int, amount: float) -> float:
        """
        WpĹaca Ĺrodki na konto uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wpĹacenia.
        :return: Aktualne saldo po wpĹacie.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if self.user.pin == pin:
            self.user.balance += amount
            return self.user.balance
        else:
            raise ValueError("Invalid pin")


    def withdraw(self, pin: int, amount: float) -> float:
        """
        WypĹaca Ĺrodki z konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wypĹacenia.
        :return: Aktualne saldo po wypĹacie.
        :raises InsufficientFundsException: JeĹli saldo jest niewystarczajÄce.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        if self.user.pin == pin:
            if self.user.balance >= amount:  # Sprawdzenie czy jest wystarczająco środków
                self.user.balance -= amount
                return self.user.balance
            else:
                raise ValueError("Insufficient funds")  # Rzucenie wyjątku zamiast pass
        else:
            raise ValueError("Invalid pin")
