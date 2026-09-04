import { useEffect, useRef } from "react";

function ChatWindow({ messages, loading }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });

    }, [messages, loading]);

    return (

        <div className="chat-messages">

            {messages.map((msg, index) => (

                <div
                    key={index}
                    className={
                        msg.role === "User"
                            ? "chat-message user-message"
                            : "chat-message assistant-message"
                    }
                >

                    <div className="message-role">
                        {msg.role === "User" ? "You" : "Chimera"}
                    </div>

                    <p className="message-content">
                        {msg.content}
                    </p>

                </div>

            ))}

            {loading && (

                <div className="chat-thinking">
                    Chimera is thinking...
                </div>

            )}

            <div ref={bottomRef} />

        </div>

    );

}

export default ChatWindow;