import DocumentUpload from "./DocumentUpload";
import ChatList from "./ChatList";

function Sidebar({

    chatId,
    setChatId,
    setMessages,

    refreshChats,
    setRefreshChats,

    onNewChat

}) {

    return (

        <>

            <h2>Chimera</h2>

            <br />

            <button
                onClick={onNewChat}
                style={{
                    width: "100%",
                    marginBottom: "15px",
                    padding: "10px"
                }}
            >
                + New Chat
            </button>

            <DocumentUpload />

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