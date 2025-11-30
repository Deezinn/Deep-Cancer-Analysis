
from langchain.messages import HumanMessage
from utils import transform_to_base64

def analisar_diagnostico(text: str, imagem: bytes = None):

    content=[
            {"type": "text", "text": text},
        ]
    
    if imagem:
        content.append({
            "type": "image_url",
            "image_url": transform_to_base64(imagem)
        })

    return HumanMessage(content=content)