from backend.services.chat_manager import ChatManager

manager = ChatManager()

chat = manager.create_chat("Testing Chat")

print(chat.to_dict())

print(manager.list_chats())