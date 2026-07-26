import ChatList from "./ChatList";

function Sidebar() {

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

            <ChatList />

        </>

    );

}

export default Sidebar;