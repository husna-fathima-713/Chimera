function ChatWindow({ messages }) {

    return (
        <div>

            {messages.map((msg, index) => (

                <div
                    key={index}
                    style={{
                        marginBottom: "20px"
                    }}
                >

                    <strong>{msg.role}</strong>

                    <p>{msg.content}</p>

                </div>

            ))}

        </div>
    );
}

export default ChatWindow;