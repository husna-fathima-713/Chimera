import ChatList from "./ChatList";

import { createChat } from "../services/chatListService";

function Sidebar({
    chatId,
    setChatId,
    setMessages,
    refreshChats
}) {

    async function handleNewChat() {

        try {

            const chat = await createChat();

            setChatId(chat.id);

            setMessages([]);

            refreshChats();

        }

        catch (error) {

            console.error(error);

        }

    }

    return (

        <>

            <h2
                style={{
                    marginBottom: "20px"
                }}
            >
                Chimera
            </h2>

            <button
                onClick={handleNewChat}
                style={{
                    padding: "12px",
                    borderRadius: "8px",
                    background: "#343541",
                    color: "white",
                    marginBottom: "20px",
                    width: "100%"
                }}
            >
                + New Chat
            </button>

            <ChatList
                chatId={chatId}
                setChatId={setChatId}
                setMessages={setMessages}
                refreshChats={refreshChats}
            />

        </>

    );

}

export default Sidebar;