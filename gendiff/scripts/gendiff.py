"""A gendiff utility startup script."""
import argparse

from gendiff import generate_diff
from gendiff.formatters.formatter import DEFAULT_FORMAT, FORMATS


def main():
    """Launch a gendiff cli."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    output_format = args.format
    if not output_format or output_format not in FORMATS.keys():
        output_format = DEFAULT_FORMAT

    diff = generate_diff(
        args.first_file, args.second_file, fmt=output_format,
    )
    print(diff)


if __name__ == '__main__':
    main()
