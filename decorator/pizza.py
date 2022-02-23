from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def do_pizza(self) -> str:
        pass


class TomatoPizza(Pizza):
    def do_pizza(self) -> str:
        return "Doing tomato pizza"


class ChickenPizza(Pizza):
    def do_pizza(self) -> str:
        return "Doing chicken pizza"



