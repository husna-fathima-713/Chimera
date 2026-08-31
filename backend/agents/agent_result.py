class AgentResult:

    def __init__(
        self,
        success,
        output,
        tool=None,
        input=None,
        reason=None,
        confidence=None
    ):

        self.success = success
        self.output = output
        self.tool = tool
        self.input = input
        self.reason = reason
        self.confidence = confidence

    def to_dict(self):

        return {
            "success": self.success,
            "tool": self.tool,
            "input": self.input,
            "output": self.output,
            "reason": self.reason,
            "confidence": self.confidence
        }