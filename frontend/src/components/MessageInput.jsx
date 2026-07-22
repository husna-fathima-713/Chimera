import { useState } from "react";

function MessageInput({ onSend }) {

    const [message, setMessage] = useState("");

    function handleSend() {

        if (!message.trim()) return;

        console.log("Sending:", message);

        onSend(message);

        setMessage("");
    }

    return (
        <div style={{ display: "flex", gap: "10px" }}>
            <input
                type="text"
                placeholder="Type a message..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                style={{
                    flex: 1,
                    padding: "12px"
                }}
            />

            <button onClick={handleSend}>
                Send
            </button>
        </div>
    );
}

export default MessageInput;