import api from "../api/api";

export async function createChat() {

    const response = await api.post("/chats");

    return response.data;

}

export async function getChats() {

    const response = await api.get("/chats");

    return response.data;

}

export async function loadChat(chatId) {

    const response = await api.get(`/chats/${chatId}`);

    return response.data;

}

export async function sendMessage(chatId, prompt) {

    const response = await api.post("/chat", {
        chat_id: chatId,
        prompt: prompt,
    });

    return response.data.response;

}