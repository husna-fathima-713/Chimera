from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = ""
    description = ""

    @abstractmethod
    def execute(self, input_data):
        """
        Execute the tool.
        """
        pass