#!/usr/bin/env python3

from sys import argv

parsed = argv[1].split(".")
release = "stable"
if len(parsed[-1]) > 1:
    release = parsed.pop(-1)
print(f"{'.'.join(parsed)}.{release if release else 'stable'}")
