"""Builder of the internal compare representation."""


def compare(dict1: dict, dict2: dict) -> list:
    """
    Generate a diff for a given dictionaries.

    Parameters:
        dict1: The first dictionary to compare.
        dict2: The second dictionary to compare.

    Returns:
        Diff of the given dictionaries.
    """
    all_keys = dict1.keys() | dict2.keys()
    removed_keys = dict1.keys() - dict2.keys()
    added_keys = dict2.keys() - dict1.keys()

    diff = []

    for key in all_keys:
        if key in removed_keys:
            diff.append(
                _generate_diff_row(
                    key, dict1[key], 'removed',
                ),
            )
        elif key in added_keys:
            diff.append(
                _generate_diff_row(
                    key, dict2[key], 'added',
                ),
            )
        elif dict1[key] == dict2[key]:
            diff.append(
                _generate_diff_row(
                    key, dict1[key], 'unmodified',
                ),
            )
        else:
            diff.append(
                _generate_diff_row(
                    key, {'old': dict1[key], 'new': dict2[key]}, 'updated',
                ),
            )

    return sorted(diff, key=lambda row: row['key'])


def _generate_diff_row(diff_key, diff_value, diff_state):
    return {'key': diff_key, 'value': diff_value, 'state': diff_state}
