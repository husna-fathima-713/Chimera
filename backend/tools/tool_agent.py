from backend.tools.registry import ToolRegistry


class ToolAgent:

    def __init__(self):
        self.registry = ToolRegistry()

    def process(self, prompt: str):

        # Future tool-selection logic goes here.

        return None