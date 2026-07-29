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

            refreshChats(chat.id);

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
                onClick={handleNewChat}
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