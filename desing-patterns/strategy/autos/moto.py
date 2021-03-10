from .auto_interface import IAuto


class Moto(IAuto):

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def locomover(self):
        return f" Moto {self.nome} esta se locomovendo"

    def ligar(self):
        return f"MOto esta ligando"