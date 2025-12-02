# src/service/pipeline.py

from typing import Optional

from .llm import MODELO
from .multimodal_chain import analisar_diagnostico


def gerar_relatorio_llm(
    prob_tumor: Optional[float],
    texto_contexto: str,
    imagem_bytes: Optional[bytes] = None,
) -> str:
    """
    Usa o Gemini (via LangChain) para gerar um relatório de apoio ao médico.

    Dois modos de uso:

    1) Com probabilidade + (opcional) imagem:
       - prob_tumor != None
       - texto_contexto: texto clínico adicional

    2) Somente texto:
       - prob_tumor == None
       - texto_contexto: pergunta ou descrição que o usuário forneceu
    """

    texto_base = ""

    # MODO 1: com probabilidade do modelo
    if prob_tumor is not None:
        prob_percent = round(prob_tumor * 100, 1)

        texto_base += (
            "Um modelo de deep learning para detecção de tumor cerebral estimou "
            f"uma probabilidade de aproximadamente {prob_percent}% de presença de tumor nesta imagem.\n\n"
        )

        if texto_contexto:
            texto_base += (
                "Informações clínicas adicionais fornecidas pelo usuário:\n"
                f"{texto_contexto}\n\n"
            )

        texto_base += (
            "Considere essa probabilidade como um indicativo e não como diagnóstico definitivo. "
            "A partir dessas informações, faça uma análise detalhada conforme suas instruções de sistema, "
            "focando em achados relevantes, limitações do modelo, hipóteses diferenciais e pontos de atenção."
        )

    # MODO 2: apenas texto (sem probabilidade / sem modelo de imagem)
    else:
        texto_base += (
            "Você recebeu um texto do usuário com dúvidas ou descrições relacionadas a "
            "tumores cerebrais ou ao sistema nervoso central.\n\n"
        )

        if texto_contexto:
            texto_base += "Texto do usuário:\n" + texto_contexto + "\n\n"

        texto_base += (
            "Responda de forma clara e organizada, conforme suas instruções de sistema, "
            "explicando conceitos, possibilidades gerais, limitações e orientando o usuário a "
            "buscar avaliação presencial com um médico. Não tente estabelecer diagnóstico pessoal."
        )

    messages = analisar_diagnostico(texto_base, imagem=imagem_bytes)
    resposta = MODELO.invoke(messages)

    # dependendo da versão do LangChain / ChatGoogleGenerativeAI:
    # pode ser resposta.content ou resposta["content"]
    return getattr(resposta, "content", str(resposta))
