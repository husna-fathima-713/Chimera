import importlib
import inspect
import pkgutil

import backend.tools


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self._discover_tools()

    def _discover_tools(self):

        package = backend.tools

        for _, module_name, _ in pkgutil.iter_modules(
            package.__path__
        ):

            if module_name == "registry":
                continue

            module = importlib.import_module(
                f"backend.tools.{module_name}"
            )

            for _, obj in inspect.getmembers(
                module,
                inspect.isclass
            ):

                if (
                    hasattr(obj, "name")
                    and hasattr(obj, "description")
                    and hasattr(obj, "execute")
                ):

                    instance = obj()

                    self.register(instance)

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return [

            {
                "name": tool.name,
                "description": tool.description
            }

            for tool in self.tools.values()

        ]