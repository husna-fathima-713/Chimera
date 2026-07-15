from backend.services.chat_manager import ChatManager

manager = ChatManager()

chat = manager.create_chat("Testing Chat")

print("Created:")
print(chat.to_dict())

print("\nAvailable Chats:")
print(manager.list_chats())

print("\nLoaded Chat:")
print(manager.load_chat(chat.id))