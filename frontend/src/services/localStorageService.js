export function saveCurrentChat(chatId) {

    localStorage.setItem(
        "chimera_current_chat",
        chatId
    );

}

export function getCurrentChat() {

    return localStorage.getItem(
        "chimera_current_chat"
    );

}

export function clearCurrentChat() {

    localStorage.removeItem(
        "chimera_current_chat"
    );

}