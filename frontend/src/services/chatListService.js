import api from "../api/api";

export async function createChat() {

    const response = await api.post("/chats");

    return response.data;

}

export async function getChats() {

    const response = await api.get("/chats");

    return response.data;

}

export async function getChat(chatId) {

    const response = await api.get(`/chats/${chatId}`);

    return response.data;

}

export async function deleteChat(chatId) {

    await api.delete(`/chats/${chatId}`);

}