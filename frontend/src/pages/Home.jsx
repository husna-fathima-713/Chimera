import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import MessageInput from "../components/MessageInput";
import DocumentUpload from "../components/DocumentUpload";

import { sendMessage } from "../services/chatService";
import { getChats, getChat } from "../services/chatListService";

function Home() {

    const [messages, setMessages] = useState([]);

    const [chatId, setChatId] = useState(null);

    const [refreshChats, setRefreshChats] = useState(false);

    function reloadChats() {
        setRefreshChats(prev => !prev);
    }

    useEffect(() => {

        async function loadLatestChat() {

            try {

                const chats = await getChats();

                if (chats.length === 0)
                    return;

                const latest = chats[chats.length - 1];

                setChatId(latest.id);

                const data = await getChat(latest.id);

                setMessages(data.messages);

            }

            catch (error) {

                console.error(error);

            }

        }

        loadLatestChat();

    }, []);

    async function handleSend(prompt) {

        if (!chatId) {

            alert("Create or select a chat first.");

            return;

        }

        const userMessage = {

            role: "User",

            content: prompt,

        };

        setMessages(prev => [...prev, userMessage]);

        try {

            const reply = await sendMessage(chatId, prompt);

            setMessages(prev => [

                ...prev,

                {

                    role: "Chimera",

                    content: reply,

                }

            ]);

        }

        catch (error) {

            console.error(error);

        }

    }

    return (

        <div className="app">

            <aside className="sidebar">

                <Sidebar

                    chatId={chatId}

                    setChatId={setChatId}

                    setMessages={setMessages}

                    refreshChats={reloadChats}

                />

            </aside>

            <main className="main">

                <DocumentUpload />

                <div className="chat-window">

                    <ChatWindow

                        messages={messages}

                    />

                </div>

                <div className="message-input">

                    <MessageInput

                        onSend={handleSend}

                    />

                </div>

            </main>

        </div>

    );

}

export default Home;