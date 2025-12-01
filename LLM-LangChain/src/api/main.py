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

model = load_brain_tumor_model()
THRESHOLD_MODEL = 0.5
THRESHOLD_LLM = 0.5


@app.post("/analisar-imagem")
async def analisar_imagem(
    file: UploadFile = File(...),
    texto_clinico: str = Form(default=""),
):
    image_bytes = await file.read()

    prob, label = predict_image_bytes(model, image_bytes, threshold=THRESHOLD_MODEL)
    prob_percent = round(prob * 100, 2)
    positivo = (label == "yes")

    llm_report = None
    if prob >= THRESHOLD_LLM:
        llm_report = gerar_relatorio_llm(prob, texto_clinico, imagem_bytes=image_bytes)

    return {
        "probabilidade_tumor": prob,
        "probabilidade_tumor_percent": prob_percent,
        "classificacao_modelo": label,
        "modelo_indica_tumor": positivo,
        "llm_acionada": llm_report is not None,
        "relatorio_llm": llm_report,
    }
