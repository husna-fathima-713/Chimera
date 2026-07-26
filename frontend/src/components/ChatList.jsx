import ChatItem from "./ChatItem";

function ChatList() {

    const chats = [
        {
            id: 1,
            title: "New Chat",
            active: true,
        }
    ];

    return (

        <div
            style={{
                marginTop: "20px",
            }}
        >

            {chats.map(chat => (

                <ChatItem
                    key={chat.id}
                    title={chat.title}
                    active={chat.active}
                />

            ))}

        </div>

    );

}

export default ChatList;