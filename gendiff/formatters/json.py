"""Diff result json formatter."""
import json


def format_diff(diff: list) -> str:
    """
    Format diff resuls as a json.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, formatted as a json.
    """
    return json.dumps(diff)
