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

                messages.map((msg, index) => {

                    const isUser = msg.role.toLowerCase() === "user";

                    return (

                        <div
                            key={index}
                            style={{
                                display: "flex",
                                justifyContent: isUser
                                    ? "flex-end"
                                    : "flex-start",
                                marginBottom: "20px",
                            }}
                        >

                            <div
                                style={{
                                    maxWidth: "75%",
                                    background: isUser
                                        ? "#0b93f6"
                                        : "#2d2d2d",
                                    padding: "14px",
                                    borderRadius: "14px",
                                    whiteSpace: "pre-wrap",
                                }}
                            >

                                <strong>

                                    {

                                        isUser
                                            ? "You"
                                            : "Chimera"

                                    }

                                </strong>

                                <div
                                    style={{
                                        marginTop: "8px",
                                    }}
                                >

                                    {msg.content}

                                </div>

                            </div>

                        </div>

                    );

                })

            }

            <div ref={bottomRef}></div>

        </div>

    );

}

export default ChatWindow;