from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def create_account(self, name: str) -> None:
        pass

    @abstractmethod
    def add_amount(self, amount: int) -> int:
        pass


class VietcomBankAccount(BankAccount):
    __fee = 1500

    def __init__(self):
        self.__current_balance = 0

    def create_account(self, name: str) -> None:
        print(f"account [{name}] created, current balance: {self.__current_balance}")

    def add_amount(self, amount: int) -> int:
        self.__current_balance += amount - self.__fee
        print(f"add {amount} to VietcomBank account, fee: {self.__fee}")
        return self.__current_balance


class TechcomBankAccount(BankAccount):
    __fee = 0

    def __init__(self):
        self.__current_balance = 0

    def create_account(self, name: str) -> None:
        print(f"account [{name}] created, current balance: {self.__current_balance}")

    def add_amount(self, amount: int) -> int:
        self.__current_balance += amount - self.__fee
        print(f"add {amount} to TechcomBank account, fee: {self.__fee}")
        return self.__current_balance


def bank_factory(bank="VietcomBank") -> BankAccount:
    if "VietcomBank" == bank:
        return VietcomBankAccount()
    elif "TechcomBank" == bank:
        return TechcomBankAccount()
    else:
        raise Exception("No instance of bank found")


if __name__ == "__main__":
    bank_account = bank_factory("TechcomBank")
    bank_account.add_amount(10000)
