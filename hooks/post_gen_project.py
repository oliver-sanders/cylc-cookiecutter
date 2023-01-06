#!/usr/bin/env python
from pathlib import Path
from shutil import rmtree


def remove(path):
    _path = Path(path)
    if _path.is_dir():
        rmtree(_path)
    else:
        _path.unlink()


if __name__ == '__main__':
    if '{{ cookiecutter.use_rose_configurations }}' != 'yes':
        remove('rose-suite.conf')
        remove('app')
