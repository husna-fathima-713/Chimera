import { useEffect, useRef } from "react";

function ChatWindow({ messages }) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
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
                            borderRadius: "8px",
                            background:
                                msg.role === "User"
                                    ? "#2d2d2d"
                                    : "#353535"
                        }}
                    >

                        <strong>
                            {msg.role}
                        </strong>

                        <p
                            style={{
                                marginTop: "8px"
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