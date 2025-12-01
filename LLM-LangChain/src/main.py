from service.multimodal_chain import analisar_diagnostico
from service.llm import MODELO

message = analisar_diagnostico(text='Fale sobre o cancer', imagem='')

result_local = MODELO.invoke(message)

print(result_local.content)