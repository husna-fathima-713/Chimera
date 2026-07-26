import { useEffect, useState } from "react";

import ChatItem from "./ChatItem";

import { getChats } from "../services/chatListService";

function ChatList() {

    const [chats, setChats] = useState([]);

    useEffect(() => {

        loadChats();

    }, []);

    async function loadChats() {

        try {

            const data = await getChats();

            setChats(data);

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

            {chats.map(chat => (

                <ChatItem
                    key={chat.id}
                    title={chat.title}
                    active={false}
                />

            ))}

        </div>

    );

}

export default ChatList;