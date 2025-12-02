from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from src.utils import transform_to_base64
from .prompt import SYSTEM_PROMPT


def analisar_diagnostico(text: str, imagem: bytes = None):
    """
    Monta as mensagens para o modelo Gemini:
    - SYSTEM: instruções do agente (SYSTEM_PROMPT)
    - HUMAN: texto clínico + (opcional) imagem em base64 como image_url
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
    ]

    # Blocos de conteúdo do usuário (texto + opcionalmente imagem)
    content_parts = [
        {
            "type": "text",
            "text": text or "Analisar o caso a seguir.",
        }
    ]

    if imagem:
        # transforma bytes em base64 e monta data URL
        b64_image = transform_to_base64(imagem)
        content_parts.append(
            {
                "type": "image_url",
                "image_url": {
                    # Gemini via LangChain aceita data URL dessa forma
                    "url": f"data:image/jpeg;base64,{b64_image}"
                },
            }
        )

    # Um único HumanMessage com lista de partes
    messages.append(HumanMessage(content=content_parts))

    return messages
