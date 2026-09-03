"""
LLM-based exception analysis for Chimera Finance Controller.

The deterministic reconciliation engine identifies financial issues.
This module uses the LLM only to explain, prioritize, and recommend
actions for those already-detected issues.
"""

from __future__ import annotations

import json
from typing import Any

from backend.models.manager import ModelManager


class ExceptionAnalyzer:

    def __init__(self):
        self.model = ModelManager()

    def analyze(
        self,
        exception: dict[str, Any],
    ) -> dict[str, Any]:

        prompt = self._build_prompt(exception)

        response = self.model.generate(
            [
                {
                    "role": "system",
                    "content": (
                        "You are a financial operations analyst.\n"
                        "Analyze only the exception provided.\n"
                        "Do not perform financial calculations.\n"
                        "Do not change or invent transaction data.\n\n"
                        "Return ONLY valid JSON using this format:\n"
                        "{"
                        '"severity": "LOW|MEDIUM|HIGH", '
                        '"explanation": "short explanation", '
                        '"recommended_action": "short action"'
                        "}"
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )

        return self._parse_response(response)

    def _build_prompt(
        self,
        exception: dict[str, Any],
    ) -> str:

        return (
            "Explain this detected reconciliation exception.\n\n"
            f"{json.dumps(exception, indent=2)}"
        )

    def _parse_response(
        self,
        response: str,
    ) -> dict[str, Any]:

        try:
            data = json.loads(response.strip())

        except json.JSONDecodeError:

            return {
                "severity": "MEDIUM",
                "explanation": response.strip(),
                "recommended_action": "Review the exception manually.",
            }

        if not isinstance(data, dict):

            return {
                "severity": "MEDIUM",
                "explanation": str(response).strip(),
                "recommended_action": "Review the exception manually.",
            }

        return {
            "severity": data.get("severity", "MEDIUM"),
            "explanation": data.get(
                "explanation",
                "Exception requires review.",
            ),
            "recommended_action": data.get(
                "recommended_action",
                "Review the exception manually.",
            ),
        }