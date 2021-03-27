from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def __init__(self):
        self.nome: str = ""
        self.massa: str = ""
        self.molho: str = ""
        self.coberturas: list[str] = []

    def preparar(self) -> None:
        print(f"Preparar {self.nome}")
        print("Jogando massa...")
        print("Adicionando molho...")
        print("Adicionando coberturas:")
        for cobertura in self.coberturas:
            print(f"{cobertura}")

    def obter_nome(self) -> str:
        return self.nome

    def assar(self) -> None:
        print("Asse por 25 minutos a 350 graus")

    def cortar(self) -> None:
        print("Corte a pizza em fatias diagonais")

    def caixa(self) -> None:
        print("Coloque a pizza na caixa oficial da PizzaStore")

    def __str__(self) -> str:
        unir_coberturas = "\n".join(self.coberturas)
        return (
            f"--- {self.nome} ---\n"
            f"{self.massa}\n"
            f"{self.molho}\n"
            f"{unir_coberturas}\n"
        )


class PizzaDesconhecida(Pizza):
    def __init__(self):
        super().__init__()
        self.nome = "Pizza de Queijo e Molho Estilo NY"
        self.massa = "Massa de Crosta Fina"
        self.molho = "Molho marinara"

        self.coberturas.append("Queijo Reggiano Ralado")


class PizzaVeggieEstiloNY(Pizza):
    def __init__(self):
        super().__init__()
        self.nome = "Pizza Veggie Estilo NY"
        self.massa = "Massa de Crosta Fina"
        self.molho = "Molho marinara"

        self.coberturas.append("Queijo Reggiano Ralado")
        self.coberturas.append("Alho")
        self.coberturas.append("Cebola")
        self.coberturas.append("Cogumelos")
        self.coberturas.append("Pimentão vermelho")


class PizzaDeQueijoEstiloChicago(Pizza):
    def __init__(self):
        super().__init__()
        self.nome = "Pizza de Queijo Estilo Chicago"
        self.massa = "Massa de Crosta Extra Espessa"
        self.molho = "Molho de tomate ameixa"

        self.coberturas.append("Queijo Mussarela Ralado")

    def cortar(self) -> None:
        print("Cortando a pizza em fatias quadradas")
