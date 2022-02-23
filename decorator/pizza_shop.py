from pizza_decorator import CheeseDecorator, PizzaDecorator, PepperDecorator
from pizza import Pizza, TomatoPizza, ChickenPizza

if __name__ == '__main__':
    tomato_pizza: Pizza = TomatoPizza()
    chicken_pizza: Pizza = ChickenPizza()

    print(tomato_pizza.do_pizza())
    print(chicken_pizza.do_pizza())

    print('add decorator -----------')

    tomato_cheese_decorator: PizzaDecorator = CheeseDecorator(tomato_pizza)
    tomato_pepper_decorator: PizzaDecorator = PepperDecorator(tomato_pizza)
    chicken_cheese_decorator: PizzaDecorator = CheeseDecorator(chicken_pizza)
    chicken_pepper_decorator: PizzaDecorator = PepperDecorator(chicken_pizza)

    print(tomato_cheese_decorator.do_pizza())
    print(tomato_pepper_decorator.do_pizza())
    print(chicken_cheese_decorator.do_pizza())
    print(chicken_pepper_decorator.do_pizza())
