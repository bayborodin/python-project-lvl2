"""A gendiff utility startup script."""
import argparse

from gendiff import generate_diff
from gendiff.formatters.formatter import DEFAULT_FORMAT


def main():
    """Launch a gendiff cli."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    diff = generate_diff(
        args.first_file, args.second_file, format=DEFAULT_FORMAT,
    )
    print(diff)


if __name__ == '__main__':
    main()
