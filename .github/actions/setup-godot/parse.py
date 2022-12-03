#!/usr/bin/env python3

from packaging.version import parse
from sys import argv

parsed = parse(argv[1])
release = argv[1].replace(
    parsed.base_version, '').strip('.')
print(f"{parsed.base_version}.{release if release else 'stable'}")
