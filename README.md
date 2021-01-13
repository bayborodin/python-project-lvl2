# Gendiff
[![Github Actions Status](https://github.com/bayborodin/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/bayborodin/python-project-lvl2/actions)
[![Actions Status](https://github.com/bayborodin/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/bayborodin/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a4bb2bcb4ba0d791eb18/maintainability)](https://codeclimate.com/github/bayborodin/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5e093a070ad425fe62f1/test_coverage)](https://codeclimate.com/github/bayborodin/python-project-lvl2/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The second training project on the Python Software Development course on [Hexlet.io](https://ru.hexlet.io/professions/python/projects/50)


## How to install
```bash
pip install git+https://github.com/bayborodin/python-project-lvl2
```

## Usage
Getting help:
```bash
gendiff -h
```

Run with the default output format (stylish):
```bash
gendiff first_file second_file
```

You can also specify the format explicitly.
Gendiff supports the output of the file comparison result in the following formats:
* stylish output (```--format=stylish```)
* plain text output (```--format=playn```)
* json output (```--format=json```)

## Demo
Getting help

[![asciicast](https://asciinema.org/a/382499.svg)](https://asciinema.org/a/382499)

Compare files (YAML and JSON formats are supported)

[![asciicast](https://asciinema.org/a/382500.svg)](https://asciinema.org/a/382500)

Manage an output format

[![asciicast](https://asciinema.org/a/382501.svg)](https://asciinema.org/a/382501)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Before sending a pull request, please make sure that all tests pass and that the linter has no comments on your code.

Please, use ```make test``` and ```make lint``` commands for this purpose.

## License
[MIT](https://choosealicense.com/licenses/mit/)
