import platform
import sys

from backend.tools.base import BaseTool


class SystemInfoTool(BaseTool):

    name = "system_info"

    description = (
        "Return basic information about the operating system "
        "and Python runtime."
    )

    def execute(self, expression=None):

        return {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "python": sys.version.split()[0]
        }