function ChatItem({ title, active }) {

    return (

        <div
            style={{
                padding: "12px",
                marginBottom: "8px",
                borderRadius: "8px",
                background: active ? "#343541" : "transparent",
                cursor: "pointer",
                transition: "0.2s"
            }}
        >
            {title}
        </div>

    );

}

export default ChatItem;