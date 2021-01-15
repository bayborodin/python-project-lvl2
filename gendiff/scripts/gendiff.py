"""A gendiff utility startup script."""
import argparse
import sys

from gendiff import generate_diff
from gendiff.formatters.formatter import DEFAULT_FORMAT, FORMATS


def main():
    """Launch a gendiff cli."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        choices=FORMATS.keys(),
        default=DEFAULT_FORMAT,
        help='set format of output',
    )

    args = parser.parse_args()
    output_format = args.format

    try:
        diff = generate_diff(
            args.first_file, args.second_file, format_name=output_format,
        )
    except ValueError as ex:  # except Exeption
        print('Something bad happend: {0}'.format(ex))
        sys.exit(1)

    print(diff)


if __name__ == '__main__':
    main()
