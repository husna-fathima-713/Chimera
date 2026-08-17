from backend.agents.tool_agent import ToolAgent


class ToolService:

    def __init__(self):

        self.agent = ToolAgent()

    def process(self, prompt):

        return self.agent.process(prompt)