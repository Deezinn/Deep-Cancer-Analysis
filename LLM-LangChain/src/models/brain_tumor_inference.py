import os
import io
import numpy as np
from PIL import Image

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input as efficientnet_preprocess

# BASE_DIR = .../src
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Agora a pasta é 'models'
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "best_transfer_model.h5")

IMG_SIZE = (224, 224)
CLASS_NAMES = ["no", "yes"]


def load_brain_tumor_model():
    """Carrega o modelo treinado (.h5)."""
    print("Procurando modelo em:", MODEL_PATH)
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Modelo não encontrado em {MODEL_PATH}")
    model = load_model(MODEL_PATH)
    print("Modelo de tumor cerebral carregado com sucesso.")
    return model


def predict_image_bytes(model, image_bytes: bytes, threshold: float = 0.5):
    """
    Faz a predição a partir de bytes de imagem.
    Retorna (prob_tumor, label), onde:
    - prob_tumor: float entre 0 e 1
    - label: 'yes' ou 'no'
    """
    # 1. Abrir e preparar a imagem
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = np.array(img, dtype="float32")
    img_array = np.expand_dims(img_array, axis=0)

    # 2. Pré-processar igual ao Colab (EfficientNet)
    img_preprocessed = efficientnet_preprocess(img_array.copy())

    # 3. Rodar o modelo
    prob = model.predict(img_preprocessed, verbose=0)[0][0]

    # 4. Converter para classe binária
    label_idx = int(prob >= threshold)
    label = CLASS_NAMES[label_idx]  # 'no' (0) ou 'yes' (1)

    return float(prob), label
