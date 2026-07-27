function ChatItem({ chat, active, onClick }) {

    return (

        <div
            onClick={onClick}
            style={{
                padding: "12px",
                marginBottom: "8px",
                borderRadius: "8px",
                background: active ? "#343541" : "transparent",
                cursor: "pointer"
            }}
        >
            {chat.title}
        </div>

    );

}

export default ChatItem;