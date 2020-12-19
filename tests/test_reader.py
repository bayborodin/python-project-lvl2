import pytest

from gendiff.reader import read_data


def test_unsupported_file_extension():
    with pytest.raises(ValueError):
        read_data('tests/fixtures/input_unknown/data1.xlsx')
