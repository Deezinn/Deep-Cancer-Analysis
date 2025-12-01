# src/service/pipeline.py

from typing import Optional

from .llm import MODELO
from .multimodal_chain import analisar_diagnostico


def gerar_relatorio_llm(prob_tumor: float, texto_contexto: str, imagem_bytes: Optional[bytes] = None) -> str:
    """
    Usa o Gemini (via LangChain) para gerar um relatório de apoio ao médico,
    com base na probabilidade estimada e em um texto adicional opcional.
    """
    prob_percent = round(prob_tumor * 100, 1)

    texto_base = (
        f"Um modelo de deep learning para detecção de tumor cerebral estimou "
        f"uma probabilidade de aproximadamente {prob_percent}% de presença de tumor nesta imagem.\n\n"
    )

    if texto_contexto:
        texto_base += "Informações clínicas adicionais fornecidas:\n" + texto_contexto + "\n\n"

    texto_base += (
        "Considere essa probabilidade como um indicativo e não como diagnóstico definitivo. "
        "A partir dessas informações, faça uma análise detalhada conforme suas instruções de sistema."
    )

    messages = analisar_diagnostico(texto_base, imagem=imagem_bytes)
    resposta = MODELO.invoke(messages)
    # dependendo da versão do LangChain / ChatGoogleGenerativeAI:
    # pode ser resposta.content ou resposta["content"]
    return getattr(resposta, "content", str(resposta))
