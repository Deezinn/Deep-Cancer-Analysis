from src.core.interfaces import ExtractInterface
from src.core.shared import URL_API_BRAIN_TUMOR

import kagglehub

class ExtractKaggle(ExtractInterface):
    def __init__(self, api_url):
        self.__api_url = api_url
    
    @classmethod
    def load_api_url(cls):
        
        if not URL_API_BRAIN_TUMOR:
            print("Não conseguimos encontrar a url para fazer a extração das imagens")
            return None
            
        if not isinstance(URL_API_BRAIN_TUMOR, str):
            print(f"O conteúdo da url está em um formato estranho, verifique se é uma string {type(URL_API_BRAIN_TUMOR)}")
            return None
        
        try:
           return cls(api_url=URL_API_BRAIN_TUMOR)
        except Exception as e:
           print(f"Erro ao capturar a url {e}")
          

    def fetch_data(self):
        try:
            path = kagglehub.dataset_download(self.__api_url)
            # print(f"O conteúdo do dataset foi baixado com sucesso, caminho {path}")
            return path
        except Exception as e:
            print(f"Erro ao extrair os dados {e}")
            return None
        
        