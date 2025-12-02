from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from src.models.brain_tumor_inference import load_brain_tumor_model, predict_image_bytes
from src.service.pipeline import gerar_relatorio_llm

app = FastAPI(title="Brain Tumor + LLM API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # em produção, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega modelo de imagem (para quando houver arquivo)
model = load_brain_tumor_model()
THRESHOLD_MODEL = 0.5
THRESHOLD_LLM = 0.5


@app.post("/analisar-imagem")
async def analisar_imagem(
    file: UploadFile | None = File(None),
    texto_clinico: str = Form(default=""),
):
    """
    Comportamento:

    - Se vier arquivo de imagem (`file`):
        -> roda o modelo de deep learning
        -> se probabilidade >= THRESHOLD_LLM, aciona LLM com probabilidade + texto + imagem

    - Se NÃO vier arquivo (somente texto_clinico):
        -> NÃO roda modelo de imagem
        -> aciona apenas a LLM usando o texto_clinico
    """

    texto_clinico = texto_clinico or ""

    # =========================
    # 1) Caso SEM IMAGEM: só texto -> LLM pura
    # =========================
    if file is None or file.filename == "":
        if not texto_clinico.strip():
            # Nada pra analisar
            return {
                "erro": "Envie pelo menos o campo 'texto_clinico' ou um arquivo de imagem."
            }

        llm_report = gerar_relatorio_llm(
            prob_tumor=None,               # sem probabilidade, modo texto-apenas
            texto_contexto=texto_clinico,
            imagem_bytes=None,
        )

        return {
            "modo": "somente_texto",
            "probabilidade_tumor": None,
            "probabilidade_tumor_percent": None,
            "classificacao_modelo": None,
            "modelo_indica_tumor": None,
            "llm_acionada": True,
            "relatorio_llm": llm_report,
        }

    # =========================
    # 2) Caso COM IMAGEM: modelo + (talvez) LLM
    # =========================
    image_bytes = await file.read()

    prob, label = predict_image_bytes(model, image_bytes, threshold=THRESHOLD_MODEL)
    prob_percent = round(prob * 100, 2)
    positivo = (label == "yes")

    llm_report = None
    if prob >= THRESHOLD_LLM:
        llm_report = gerar_relatorio_llm(
            prob_tumor=prob,
            texto_contexto=texto_clinico,
            imagem_bytes=image_bytes,
        )

    return {
        "modo": "imagem+modelo",
        "probabilidade_tumor": prob,
        "probabilidade_tumor_percent": prob_percent,
        "classificacao_modelo": label,
        "modelo_indica_tumor": positivo,
        "llm_acionada": llm_report is not None,
        "relatorio_llm": llm_report,
    }
