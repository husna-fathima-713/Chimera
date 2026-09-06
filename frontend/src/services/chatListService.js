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


export async function renameChat(chatId, title) {

    const response = await api.put(
        `/chats/${chatId}/rename`,
        {
            title: title
        }
    );

    return response.data;

}


export async function deleteChat(chatId) {

    await api.delete(`/chats/${chatId}`);

}