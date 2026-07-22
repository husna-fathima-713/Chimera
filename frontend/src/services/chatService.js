import api from "../api/api";

export async function sendMessage(chatId, prompt) {

    console.log("Calling backend...");
    console.log({
        chat_id: chatId,
        prompt: prompt,
    });

    const response = await api.post("/chat", {
        chat_id: chatId,
        prompt: prompt,
    });

    console.log("Backend Response:", response);

    return response.data.response;
}