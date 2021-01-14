"""Diff output format selector."""
import types

from gendiff.formatters import json, plain, stylish

DEFAULT_FORMAT = 'stylish'

FORMATS = types.MappingProxyType({
    'stylish': stylish,
    'plain': plain,
    'json': json,
})


def format_diff(diff: list, style: str = DEFAULT_FORMAT) -> str:
    """
    Format the diff output with a given format style.

    Parameters:
        diff: A files file structures compare result.
        style: A formatter name to format a diff.

    Returns:
        A formatted diff.

    Raises:
        ValueError: When the unknown format key is given.
    """
    if style in FORMATS.keys():
        return FORMATS.get(style).format_diff(diff)
    raise ValueError('Unknown diff output format!')
