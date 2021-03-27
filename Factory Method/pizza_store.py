from abc import ABC, abstractmethod
from pizza import (
    PizzaDesconhecida,
    PizzaVeggieEstiloNY,
    PizzaDeQueijoEstiloChicago,
    Pizza
)


class LojaPizza(ABC):
    @abstractmethod
    def criar_pizza(self, sabor: str) -> Pizza:
        raise NotImplementedError

    def pedir_pizza(self, sabor: str) -> Pizza:
        pizza = self.criar_pizza(sabor)
        pizza.preparar()
        pizza.assar()
        pizza.cortar()
        pizza.caixa()
        return pizza


class LojaPizzaChicago(LojaPizza):
    def criar_pizza(self, sabor: str) -> Pizza:
        if sabor == "queijo":
            return PizzaDeQueijoEstiloChicago()
        elif sabor == "veggie":
            return PizzaVeggieEstiloNY()
        return PizzaDesconhecida()

