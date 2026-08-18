from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = ""
    description = ""

    def run(self, prompt):

        try:

            result = self.execute(prompt)

            return {
                "success": True,
                "tool": self.name,
                "input": prompt,
                "output": result
            }

        except Exception as exc:

            return {
                "success": False,
                "tool": self.name,
                "input": prompt,
                "output": str(exc)
            }

    @abstractmethod
    def execute(self, prompt):
        pass