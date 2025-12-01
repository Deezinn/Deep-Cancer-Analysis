import axios from "axios";

const api = axios.create({
    baseURL: '',
    withCredentials: true,
    credentials: "same-origin"
})

export default api;