#!/usr/bin/env python3

import re
import sys

platform = f'"{sys.argv[1]}"'

with open('export_presets.cfg', "r") as f:
    export_presets = f.read()
    regex = r'\[preset.[0-9]\]\n+name="([A-Za-z0-9]+)"\n+platform=' + platform
    matches = re.search(
        regex, export_presets)
    if matches:
        print(matches.groups()[0])
    else:
        sys.exit(1)
