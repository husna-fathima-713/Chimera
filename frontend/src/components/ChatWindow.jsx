import { useEffect, useRef } from "react";

function ChatWindow({ messages }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });

    }, [messages]);

    return (

        <div>

            {

                messages.map((msg, index) => (

                    <div
                        key={index}
                        style={{
                            marginBottom: "20px",
                            padding: "12px",
                            background: "#2b2d31",
                            borderRadius: "8px",
                        }}
                    >

                        <strong>
                            {msg.role}
                        </strong>

                        <p
                            style={{
                                marginTop: "8px",
                                whiteSpace: "pre-wrap",
                            }}
                        >
                            {msg.content}
                        </p>

                    </div>

                ))

            }

            <div ref={bottomRef} />

        </div>

    );

}

export default ChatWindow;