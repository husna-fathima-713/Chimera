import importlib
import inspect
import pkgutil

import backend.tools

from backend.tools.base import BaseTool


class ToolRegistry:

    def __init__(self):

        self.tools = {}

        self._discover_tools()

    def _discover_tools(self):

        package = backend.tools

        for _, module_name, _ in pkgutil.iter_modules(
            package.__path__
        ):

            if module_name in (
                "registry",
                "base"
            ):
                continue

            module = importlib.import_module(
                f"backend.tools.{module_name}"
            )

            for _, obj in inspect.getmembers(
                module,
                inspect.isclass
            ):

                if (
                    inspect.isclass(obj)
                    and issubclass(obj, BaseTool)
                    and obj is not BaseTool
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