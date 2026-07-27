import ChatList from "./ChatList";

import { createChat } from "../services/chatListService";

function Sidebar({
    chatId,
    setChatId,
    setMessages,
}) {

    async function handleNewChat() {

        try {

            const chat = await createChat();

            setChatId(chat.id);

            setMessages([]);

            window.location.reload();

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
                    marginBottom: "20px"
                }}
            >
                + New Chat
            </button>

            <ChatList
                chatId={chatId}
                setChatId={setChatId}
                setMessages={setMessages}
            />

        </>

    );

}

export default Sidebar;