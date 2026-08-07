from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = ""
    description = ""

    @abstractmethod
    def can_handle(self, prompt):
        pass

    @abstractmethod
    def prepare_input(self, prompt):
        """
        Convert the user's prompt into the
        input required by execute().
        """
        pass

    @abstractmethod
    def execute(self, input_data):
        pass