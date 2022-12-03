#!/usr/bin/env python3

import re
import sys

map = {
    3: {
        "android": "Android",
        "linux": "Linux/X11",
        "mac": "Mac OSX",
        "web": "HTML5",
        "windows": "Windows Desktop",
    },
    4: {
        "android": "Android",
        "linux": "Linux/X11",
        "mac": "macOS",
        "web": "Web",
        "windows": "Windows Desktop",
    }
}

platform = f'"{map[int(sys.argv[1])][sys.argv[2]]}"'

with open('export_presets.cfg', "r") as f:
    export_presets = f.read()
    regex = r'\[preset.[0-9]\]\n+name="([A-Za-z0-9]+)"\n+platform=' + platform
    matches = re.search(
        regex, export_presets)
    if matches:
        print(matches.groups()[0])
    else:
        sys.exit(1)
