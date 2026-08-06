from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = ""
    description = ""

    @abstractmethod
    def can_handle(self, prompt):
        """
        Returns True if this tool can handle the prompt.
        """
        pass

    @abstractmethod
    def execute(self, input_data):
        """
        Executes the tool.
        """
        pass