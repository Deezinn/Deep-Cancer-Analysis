from abc import ABC, abstractmethod

class ExtractInterface(ABC):
    """
    Classe que servirá como contrato de extração das imagens e dataset sobre cancêr cerebral
    """
    
    @classmethod
    @abstractmethod
    def load_api_url(self):
        """ 
        Método padrão onde a classe vai usar para extrair os dados
        """
        pass
    
    @abstractmethod
    def fetch_data(self):
        pass