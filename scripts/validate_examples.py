"""Validate CLINC150 training examples before publishing."""

from collections.abc import Iterable


def validate_examples(examples: Iterable[dict[str, str]]) -> None:
    for index, example in enumerate(examples):
        text = example.get("text", "").strip()
        intent = example.get("intent", "").strip()

        if not text or not intent:
            raise ValueError(
                f"Training example {index} requires text and intent"
            )
