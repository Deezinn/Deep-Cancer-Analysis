from service.multimodal_chain import analisar_diagnostico
from service.llm import MODELO

result_local = MODELO.invoke([analisar_diagnostico(text='O que voce acha de victor lavor? ele é personal trainer, tem um carro oroch e esta tentando entrar na area de TI, oq vc recomendaria para essa pessoa?', imagem='')])
print(result_local.content)