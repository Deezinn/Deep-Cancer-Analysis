# 🧠 Brain Tumor Detection -- Deep Learning + LLM Pipeline

Este projeto consiste em uma solução completa para **detecção de tumores
cerebrais** a partir de imagens médicas (raio-x / ressonância)
utilizando **Deep Learning**, integrada a uma **LLM** capaz de fornecer
orientações clínicas detalhadas quando há risco detectado.

A arquitetura final inclui:

-   🧬 **Modelo CNN** baseado em EfficientNetB0
-   ⚙️ **API FastAPI** para servir o modelo e integrar a LLM
-   💬 **Integração com LLM** para análises clínicas complementares
-   🌐 **Frontend em Next.js**, onde o usuário (médico) interage com o
    sistema via chat
-   🚀 **Deploy completo na Render**, com backend e frontend separados


------------------------------------------------------------------------

## 🎯 Visão Geral

O objetivo do projeto é criar um sistema capaz de:

1.  **Detectar automaticamente a probabilidade de um tumor cerebral** em
    uma imagem enviada pelo usuário.
2.  **Retornar uma análise complementar**, via LLM, quando a
    probabilidade ultrapassa determinado limiar (≥ 50%).
3.  **Permitir que médicos conversem com a IA**, enviando imagens ou
    textos para análises adicionais.

------------------------------------------------------------------------

## 🏗 Arquitetura do Projeto

A solução é dividida em 3 módulos principais:

1.  **📘 Deep Learning (Tensorflow, Keras e EfficientNet80 no Colab)**
2.  **⚙️ Backend (FastAPI)**
3.  **🌐 Frontend (Next.js)**

------------------------------------------------------------------------

## 🧬 Modelo de Deep Learning

Treinado no **Google Colab** utilizando TensorFlow, Keras e
EfficientNetB0.

Arquivo final:

`LLM-LangChain/src/models/best_transfer_model.h5`

O modelo retorna probabilidade (0--1) e classificação ("Tumor" /
"Normal").

------------------------------------------------------------------------

## ⚙️ API (FastAPI)

Local:

`LLM-LangChain/src/api/api.py`

### Endpoint principal

`POST /analisar-imagem`

Retorna:

-   Probabilidade
-   Veredito
-   Resposta da LLM (se probabilidade ≥ 50%)
-   Imagem processada

------------------------------------------------------------------------

## 💬 Integração com LLM

Acionada quando o modelo indica risco ≥ 50%.
A LLM retorna:

-   Interpretação médica inicial
-   Hipóteses diferenciais
-   Recomendações de próximos passos

------------------------------------------------------------------------

## 🌐 Frontend (Next.js)

Local:

`web-site/src/`

Funcionalidades:

-   Chat com a IA\
-   Envio de imagens\
-   Exibição das probabilidades e diagnósticos

------------------------------------------------------------------------

## 🔄 Pipeline da Requisição

1.  Usuário envia imagem/texto pelo frontend\
2.  API recebe requisição multiform\
3.  Modelo roda inferência\
4.  LLM é acionada se necessário\
5.  Frontend exibe resultados

------------------------------------------------------------------------

## 🗂 Estrutura de Pastas

    /
    ├── LLM-LangChain/
    │   ├── src/
    │   │   ├── api/api.py
    │   │   ├── models/best_transfer_model.h5
    │   │   ├── service/pipeline.py
    │
    ├── web-site/
    │   └── src/


------------------------------------------------------------------------

## 📦 Instalação e Execução Local

### Backend

    cd LLM-LangChain
    pip install -r requirements.txt
    uvicorn src.api.api:app --reload

### Frontend

    cd web-site
    npm install
    npm run dev

------------------------------------------------------------------------

## 🛠 Tecnologias Utilizadas

-   TensorFlow, Keras, EfficientNetB0
-   FastAPI, Uvicorn
-   Next.js, React
-   Render

------------------------------------------------------------------------

## 🚀 Deploy

Deploy separado na plataforma Render (API + Frontend).

------------------------------------------------------------------------

## 👥 Autores

-   Rafael Moura
-   André Nascimento
