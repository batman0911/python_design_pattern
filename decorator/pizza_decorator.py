from abc import ABC

from pizza import Pizza


class PizzaDecorator(Pizza, ABC):
    _pizza: Pizza

    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_pizza(self) -> Pizza:
        return self._pizza

    def set_pizza(self, pizza: Pizza) -> None:
        self._pizza = pizza


class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def do_pizza(self) -> str:
        pizza_type: str = self.get_pizza().do_pizza()
        return pizza_type + self.add_cheese()

    @classmethod
    def add_cheese(cls) -> str:
        return " + cheese"


class PepperDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def do_pizza(self) -> str:
        pizza_type: str = self.get_pizza().do_pizza()
        return pizza_type + self.add_pepper()

    @classmethod
    def add_pepper(cls) -> str:
        return " + pepper"
