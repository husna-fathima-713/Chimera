import { useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import MessageInput from "../components/MessageInput";

import { sendMessage } from "../services/chatService";

function Home() {

    const [messages, setMessages] = useState([]);
    const [chatId, setChatId] = useState(null);

    const [refreshChats, setRefreshChats] = useState(false);

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

    function reloadChats() {

        setRefreshChats(prev => !prev);

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