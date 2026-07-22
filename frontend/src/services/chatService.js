import api from "../api/api";

export async function sendMessage(chatId, prompt) {

    const response = await api.post("/chat", {
        chat_id: chatId,
        prompt: prompt,
    });

    return response.data.response;
}