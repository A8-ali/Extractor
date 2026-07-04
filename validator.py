"""
Validation and normalization utilities.
"""

from __future__ import annotations

import re
from typing import Any
from errors import InvalidAgeError
from schema import SCHEMA, DEFAULT_VALUES


def validate(data: dict[str, Any]) -> dict[str, Any]:
    """
    Validate and normalize extracted data.

    Args:
        data: Extracted dictionary returned by the AI.

    Returns:
        A validated and normalized dictionary.
    """

    _validate_required_fields(data)
    _validate_types(data)
    _normalize_data(data)

    return data


def _validate_required_fields(data: dict[str, Any]) -> None:
    """
    Ensure all required fields exist.
    """

    for key, default in DEFAULT_VALUES.items():
        data.setdefault(key, default)


def _validate_types(data: dict[str, Any]) -> None:
    """
    Validate field types.

    Only performs validation that cannot safely be handled by the
    normalization step.
    """

    age = data.get("age")

    if age is None:
        return

    if isinstance(age, int):
        return

    if isinstance(age, str):
        try:
            data["age"] = int(age.strip())
        except Exception as e:
            data["age"] = None
            raise InvalidAgeError(f"age must be int: {e}") from e
        return

    data["age"] = None


def _normalize_data(data: dict[str, Any]) -> None:
    """
    Normalize extracted values according to the project schema.
    """

    for key, expected_type in SCHEMA.items():

        value = data.get(key)

        # ---------- String ----------
        if expected_type is str:

            if isinstance(value, str):
                data[key] = value.strip()
            else:
                data[key] = None

        # ---------- Integer ----------
        elif expected_type is int:

            # _validate_types already handled integers.
            continue

        # ---------- List ----------
        elif expected_type is list:

            if value is None:
                data[key] = []
                continue

            if isinstance(value, str):
                value = re.split(r"[,،;\n|]+", value)

            elif not isinstance(value, list):
                data[key] = []
                continue

            data[key] = [
                item.strip()
                for item in value
                if isinstance(item, str) and item.strip()
            ]