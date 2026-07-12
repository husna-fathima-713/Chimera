from backend.models.manager import ModelManager

manager = ModelManager()

response = manager.generate("Say hello in one sentence.")

print(response)