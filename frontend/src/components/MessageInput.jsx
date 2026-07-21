function MessageInput() {
    return (
        <div>
            <input
                type="text"
                placeholder="Type a message..."
                style={{
                    width: "85%",
                    padding: "10px"
                }}
            />

            <button
                style={{
                    marginLeft: "10px",
                    padding: "10px 20px"
                }}
            >
                Send
            </button>
        </div>
    );
}

export default MessageInput;