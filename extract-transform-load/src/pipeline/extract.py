from src.core.interfaces import ExtractInterface
from src.core.shared import URL_API_BRAIN_TUMOR

import kagglehub


class Extract(ExtractInterface):
    
    def load_data(self):
       try:
            if not URL_API_BRAIN_TUMOR:
                print("Não conseguimos encontrar a url para fazer a extração das imagens")
            
            if not isinstance(URL_API_BRAIN_TUMOR, str):
                print(f"O conteúdo da url está em um formato estranho, verifique se é uma string {type(URL_API_BRAIN_TUMOR)}")

            path = kagglehub.dataset_download(URL_API_BRAIN_TUMOR)
            
            if path:
                print(f"Os arquivos foram baixados no caminho: {path}")
       except Exception:
           pass

a = Extract()
a.load_data()