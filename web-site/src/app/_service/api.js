import axios from "axios";

const api = axios.create({
    baseURL: "https://brain-tumor-llm-api.onrender.com",
});

export default api;
