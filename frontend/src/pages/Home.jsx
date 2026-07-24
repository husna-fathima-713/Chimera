import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import MessageInput from "../components/MessageInput";

function Home() {
    return (
        <>
            <Sidebar />
            <ChatWindow />
            <MessageInput />
        </>
    );
}

export default Home;