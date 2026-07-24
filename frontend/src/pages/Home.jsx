import { useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import MessageInput from "../components/MessageInput";
import DocumentUpload from "../components/DocumentUpload";

import { sendMessage } from "../services/chatService";

function Home() {

    const [messages, setMessages] = useState([]);

    const chatId = "default";

    async function handleSend(prompt) {

        const userMessage = {
            role: "User",
            content: prompt,
        };

        setMessages(prev => [...prev, userMessage]);

        try {

            const reply = await sendMessage(chatId, prompt);

            const assistantMessage = {
                role: "Chimera",
                content: reply,
            };

            setMessages(prev => [
                ...prev,
                assistantMessage,
            ]);

        }

        catch (error) {

            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    role: "System",
                    content: "Failed to contact backend.",
                },
            ]);

        }

    }

    return (

        <div className="app">

            <aside className="sidebar">

                <Sidebar />

                <hr />

                <DocumentUpload />

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