from os import path
from sys import argv

print(path.normpath((path.join("repo", argv[1]) if argv[1] else "repo")))
