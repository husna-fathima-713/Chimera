from backend.services.chat_manager import ChatManager

manager = ChatManager()

chat = manager.create_chat("Testing Chat")

manager.add_message(chat.id, "user", "Hello")

manager.add_message(chat.id, "assistant", "Hi there!")

print(manager.get_messages(chat.id))