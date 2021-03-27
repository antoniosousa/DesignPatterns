from pizza import Pizza
from pizza_store import LojaPizzaChicago


loja_chicago: LojaPizzaChicago = LojaPizzaChicago()

pizza: Pizza = loja_chicago.pedir_pizza("queijo")
print(f"Antonio pediu uma {pizza.obter_nome()}")
