import { useState } from "react";

import { renameChat } from "../services/chatListService";


function ChatItem({
    chat,
    active,
    onClick,
    onDelete
}) {

    const [isRenaming, setIsRenaming] = useState(false);
    const [title, setTitle] = useState(chat.title || "New Chat");


    function handleRenameStart(event) {

        event.stopPropagation();

        setTitle(chat.title || "New Chat");
        setIsRenaming(true);

    }


    function handleRenameCancel(event) {

        event.stopPropagation();

        setTitle(chat.title || "New Chat");
        setIsRenaming(false);

    }


    async function handleRenameSave(event) {

        event.stopPropagation();

        const newTitle = title.trim();

        if (!newTitle) {
            setTitle(chat.title || "New Chat");
            setIsRenaming(false);
            return;
        }

        if (newTitle === chat.title) {
            setIsRenaming(false);
            return;
        }

        try {

            const updatedChat = await renameChat(
                chat.id,
                newTitle
            );

            chat.title = updatedChat.title;

            setTitle(updatedChat.title);
            setIsRenaming(false);

        } catch (error) {

            console.error(error);

            setTitle(chat.title || "New Chat");
            setIsRenaming(false);

        }

    }


    function handleKeyDown(event) {

        if (event.key === "Enter") {
            handleRenameSave(event);
        }

        if (event.key === "Escape") {
            handleRenameCancel(event);
        }

    }


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
            onClick={isRenaming ? undefined : onClick}
        >

            {isRenaming ? (

                <input
                    className="chat-title-input"
                    value={title}
                    onChange={(event) => setTitle(event.target.value)}
                    onKeyDown={handleKeyDown}
                    onClick={(event) => event.stopPropagation()}
                    autoFocus
                />

            ) : (

                <span className="chat-title">
                    {chat.title || "New Chat"}
                </span>

            )}


            {isRenaming ? (

                <>

                    <button
                        className="save-chat-button"
                        onClick={handleRenameSave}
                        title="Save chat name"
                    >
                        ✓
                    </button>

                    <button
                        className="cancel-chat-button"
                        onClick={handleRenameCancel}
                        title="Cancel rename"
                    >
                        ×
                    </button>

                </>

            ) : (

                <>

                    <button
                        className="rename-chat-button"
                        onClick={handleRenameStart}
                        title="Rename chat"
                    >
                        ✎
                    </button>

                    <button
                        className="delete-chat-button"
                        onClick={handleDelete}
                        title="Delete chat"
                    >
                        ×
                    </button>

                </>

            )}

        </div>

    );

}


export default ChatItem;