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

    async function loadChats() {

        try {

            const data = await getChats();

            setChats(data);

        }

        catch (error) {

            console.error(error);

        }

    }

    useEffect(() => {

        loadChats();

    }, [refreshChats]);

    async function selectChat(chat) {

        try {

            const data = await getChat(chat.id);

            setChatId(chat.id);

            setMessages(data.messages);

        }

        catch (error) {

            console.error(error);

        }

    }

    return (

        <div
            style={{
                marginTop: "20px"
            }}
        >

            {

                chats.map(chat => (

                    <ChatItem

                        key={chat.id}

                        chat={chat}

                        active={chat.id === chatId}

                        onClick={() => selectChat(chat)}

                    />

                ))

            }

        </div>

    );

}

export default ChatList;