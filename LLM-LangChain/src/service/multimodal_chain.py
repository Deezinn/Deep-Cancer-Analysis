from .prompt import SYSTEM_PROMPT

from langchain.messages import HumanMessage, AIMessage, SystemMessage
from utils import transform_to_base64

def analisar_diagnostico(text: str, imagem: bytes = None):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=text)
    ]

    if imagem:
        messages.append(
            HumanMessage(content={
                "type": "image_url",
                "image_url": {"url": transform_to_base64(imagem)}
            })
        )

    return messages
