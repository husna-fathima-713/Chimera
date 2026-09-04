import { useEffect, useState } from "react";

import ChatItem from "./ChatItem";

import {
    getChats,
    getChat,
} from "../services/chatListService";

function ChatList({
    chatId,
    setChatId,
    setMessages,
    refreshChats
}) {

    const [chats, setChats] = useState([]);

    async function selectChat(chat) {

        try {

            const data = await getChat(chat.id);

            setChatId(chat.id);

            setMessages(data.messages || []);

        } catch (error) {

            console.error(error);

        }

    }

    async function loadChats() {

        try {

            const data = await getChats();

            const validChats = [];

            for (const chat of data) {

                try {

                    const fullChat = await getChat(chat.id);

                    if (
                        fullChat.messages &&
                        fullChat.messages.length > 0
                    ) {
                        validChats.push(chat);
                    }

                } catch (error) {

                    console.error(error);

                }

            }

            const recentChats = validChats.slice(-5);

            setChats(recentChats);

            if (
                recentChats.length > 0 &&
                !chatId
            ) {

                selectChat(recentChats[recentChats.length - 1]);

            }

        } catch (error) {

            console.error(error);

        }

    }

    function handleDelete(deletedChatId) {

        setChats(prev =>
            prev.filter(chat => chat.id !== deletedChatId)
        );

        if (deletedChatId === chatId) {

            setChatId(null);
            setMessages([]);

        }

    }

    useEffect(() => {

        loadChats();

    }, [refreshChats]);

    return (

        <div
            style={{
                marginTop: "20px"
            }}
        >

            {chats.map(chat => (

                <ChatItem
                    key={chat.id}
                    chat={chat}
                    active={chat.id === chatId}
                    onClick={() => selectChat(chat)}
                    onDelete={handleDelete}
                />

            ))}

        </div>

    );

}

export default ChatList;