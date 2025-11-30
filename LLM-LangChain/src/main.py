from service.multimodal_chain import analisar_diagnostico
from service.llm import MODELO

result_local = MODELO.invoke([analisar_diagnostico(text='oi, tudo bem?', imagem='')])
print(result_local.content)