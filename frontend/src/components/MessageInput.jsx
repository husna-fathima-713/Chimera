import { useState } from "react";

function MessageInput({ onSend }) {

    const [message, setMessage] = useState("");

    function handleSend() {

        if (!message.trim()) return;

        onSend(message);

        setMessage("");

    }

    function handleKeyDown(event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            handleSend();

        }

    }

    return (

        <div className="message-input-container">

            <input
                className="message-input-field"
                type="text"
                placeholder="Message Chimera..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={handleKeyDown}
            />

            <button
                className="send-button"
                onClick={handleSend}
                disabled={!message.trim()}
            >
                Send
            </button>

        </div>

    );

}

export default MessageInput;