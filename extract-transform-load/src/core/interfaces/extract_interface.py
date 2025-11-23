from abc import ABC, abstractmethod

class ExtractInterface(ABC):

    @classmethod
    @abstractmethod
    def load_api_url(cls):
        """
        Método que retorna a URL da API
        """
        pass

    @abstractmethod
    def fetch_data(self):
        """
        Método para buscar dados
        """
        pass
