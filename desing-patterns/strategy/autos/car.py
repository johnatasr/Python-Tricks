from .auto_interface import IAuto


class Car(IAuto):

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def locomover(self):
        return f" Carro {self.nome} esta se locomovendo"

    def ligar(self):
        return f"Carro esta ligando"