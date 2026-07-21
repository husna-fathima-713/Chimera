import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import MessageInput from "../components/MessageInput";

function Home() {
    return (
        <div className="app">

            <aside className="sidebar">
                <Sidebar />
            </aside>

            <main className="main">

                <div className="chat-window">
                    <ChatWindow />
                </div>

                <div className="message-input">
                    <MessageInput />
                </div>

            </main>

        </div>
    );
}

export default Home;