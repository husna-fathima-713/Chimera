import { useEffect, useRef } from "react";

function ChatWindow({ messages, loading }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });

    }, [messages, loading]);

    return (

        <div>

            {

                messages.map((msg, index) => (

                    <div

                        key={index}

                        style={{
                            marginBottom: "20px",
                            padding: "12px",
                            borderRadius: "8px",
                            background:
                                msg.role === "User"
                                    ? "#2d3748"
                                    : "#1f2937",
                        }}

                    >

                        <strong>{msg.role}</strong>

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

            {

                loading && (

                    <div

                        style={{
                            padding: "12px",
                            color: "#999",
                            fontStyle: "italic",
                        }}

                    >

                        Chimera is thinking...

                    </div>

                )

            }

            <div ref={bottomRef} />

        </div>

    );

}

export default ChatWindow;