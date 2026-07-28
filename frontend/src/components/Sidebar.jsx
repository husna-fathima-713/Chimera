import { useState } from "react";

import DocumentUpload from "./DocumentUpload";
import ChatList from "./ChatList";

import { createChat } from "../services/chatListService";

function Sidebar({

    chatId,
    setChatId,
    setMessages,
    refreshChats

}) {

    const [reload, setReload] = useState(false);

    async function handleCreateChat() {

        try {

            const chat = await createChat();

            setChatId(chat.id);

            setMessages([]);

            setReload(prev => !prev);

            refreshChats();

        }

        catch (error) {

            console.error(error);

        }

    }

    return (

        <>

            <h2>Chimera</h2>

            <br />

            <button
                onClick={handleCreateChat}
            >
                + New Chat
            </button>

            <br />
            <br />

            <DocumentUpload />

            <ChatList

                chatId={chatId}

                setChatId={setChatId}

                setMessages={setMessages}

                refreshChats={reload}

            />

        </>

    );

}

export default Sidebar;