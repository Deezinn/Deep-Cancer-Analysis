from abc import ABC

class ExtractInterface(ABC):
    """
    Classe que servirá como contrato de extração das imagens e dataset sobre cancêr cerebral
    """
    def load_data(self):
        """ 
        Método padrão onde a classe vai usar para extrair os dados
        """
        pass
        