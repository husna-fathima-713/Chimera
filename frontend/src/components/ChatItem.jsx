function ChatItem({
    chat,
    active,
    onClick,
    onDelete
}) {

    async function handleDelete(event) {

        event.stopPropagation();

        const confirmed = window.confirm(
            "Delete this chat? This cannot be undone."
        );

        if (!confirmed) return;

        try {

            await import("../services/chatListService")
                .then(({ deleteChat }) => deleteChat(chat.id));

            onDelete(chat.id);

        } catch (error) {

            console.error(error);

        }

    }

    return (

        <div
            className={`chat-item ${active ? "active" : ""}`}
            onClick={onClick}
        >

            <span className="chat-title">
                {chat.title || "New Chat"}
            </span>

            <button
                className="delete-chat-button"
                onClick={handleDelete}
                title="Delete chat"
            >
                ×
            </button>

        </div>

    );

}

export default ChatItem;