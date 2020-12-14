from gendiff import generate_diff


def test_diff_flat_json():
    with open("tests/fixtures/diff_flat_files_result.txt", "r") as f:
        expected = f.read().strip()

    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json").strip()

    assert result == expected


def test_diff_flat_yaml():
    with open("tests/fixtures/diff_flat_files_result.txt", "r") as f:
        expected = f.read().strip()

    result = generate_diff("tests/fixtures/file1.yml",
                           "tests/fixtures/file2.yml").strip()

    assert result == expected
