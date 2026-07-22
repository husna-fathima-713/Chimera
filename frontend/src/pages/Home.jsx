import { useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import MessageInput from "../components/MessageInput";

import { sendMessage } from "../services/chatService";

function Home() {

    const [messages, setMessages] = useState([]);

    const chatId = "default";

    async function handleSend(prompt) {

        const userMessage = {
            role: "User",
            content: prompt,
        };

        setMessages((prev) => [...prev, userMessage]);

        const reply = await sendMessage(chatId, prompt);

        const assistantMessage = {
            role: "Chimera",
            content: reply,
        };

        setMessages((prev) => [...prev, assistantMessage]);
    }

    return (

        <div className="app">

            <aside className="sidebar">
                <Sidebar />
            </aside>

            <main className="main">

                <div className="chat-window">
                    <ChatWindow messages={messages} />
                </div>

                <div className="message-input">
                    <MessageInput onSend={handleSend} />
                </div>

            </main>

        </div>

    );
}

export default Home;