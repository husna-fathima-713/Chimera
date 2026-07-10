from backend.config import MODEL_NAME


class ModelManager:

    def __init__(self):
        self.model_name = MODEL_NAME

    def current_model(self):
        return self.model_name