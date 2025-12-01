import api from './api'

export const teste = async ({text, image}) => {
    try {
        const response = await api.post(
            '',
            {
                text: text,
                image: image
            }
        )
    } catch (error) {
        throw error
    }
    return response
}