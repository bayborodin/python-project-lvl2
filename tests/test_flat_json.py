from gendiff import generate_diff


def test_different_files():
    with open("tests/fixtures/file1_file2.txt", "r") as f:
        expected = f.read().strip()

    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json").strip()

    assert result == expected
