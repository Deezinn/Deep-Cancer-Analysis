from src.core.interfaces import ExtractInterface
from src.core.shared import URL_API_DEATH_RATE

import requests

from io import StringIO

class ExtractWorldData(ExtractInterface):
    def __init__(self, api_url):
        self.__api_url = api_url
    
    @classmethod
    def load_api_url(cls):
        
        if not URL_API_DEATH_RATE:
            print("Não conseguimos encontrar a url para fazer a extração das quantidades de mortes por país")
            return None
            
        if not isinstance(URL_API_DEATH_RATE, str):
            print(f"O conteúdo da url está em um formato estranho, verifique se é uma string {type(URL_API_DEATH_RATE)}")
            return None
        
        try:
           return cls(api_url=URL_API_DEATH_RATE)
        except Exception as e:
           print(f"Erro ao capturar a url {e}")
          

    def fetch_data(self):
        try:
            r = requests.get(self.__api_url)
            if r.status_code == 200:
                return StringIO(r.text)
        except Exception as e:
            print(f"Erro ao extrair os dados {e}")
        
        