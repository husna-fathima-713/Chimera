class BaseModel:
    """
    Base interface for every AI model.
    """

    def generate(self, prompt: str) -> str:
        raise NotImplementedError