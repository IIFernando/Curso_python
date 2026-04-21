from abc import ABC, abstractmethod # Forma para utilizar interfaces abstratas

class controleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTv(controleRemoto):
    def ligar(self):
        print('Ligando a TV!')

    def desligar(self):
        print('Desligando a TV!')

controle = ControleTv()

controle.ligar()