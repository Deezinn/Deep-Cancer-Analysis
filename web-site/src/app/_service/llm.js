import api from "./api";

export const teste = async ({ text, file }) => {
    try {
        if (!file) {
            console.log("Nenhum arquivo enviado (e permitido).");
        }
        const formData = new FormData();
        formData.append("texto_clinico", text);

        if (file) {
            formData.append("file", file); 
        }
        const response = await api.post("/analisar-imagem", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            }
        });
        return response.data;

    } catch (error) {
        console.error("Erro no envio:", error.response?.data || error);
        throw error;
    }
};
