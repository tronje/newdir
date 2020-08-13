#!/usr/bin/env python3

import os
import random
import sys
import tempfile

from animals import animals
from adjectives import adjectives


def print_err(msg):
    print(msg, file=sys.stderr)


def newdir():
    try:
        adjective = random.choice(adjectives)
        animal = random.choice(animals)

        dirname = adjective + '_' + animal
        dirpath = os.path.join(tempfile.gettempdir(), dirname)

        os.mkdir(dirpath)
        return dirpath
    except FileExistsError:  # directory exists already
        return None
    except Exception as e:
        print_err(f"newdir failed with '{type(e)}: {e}'")
        sys.exit(1)


def main():
    tries = 0

    while tries < 10:
        path = newdir()
        if path is not None:
            # print to stderr so the user sees the command
            print_err(f"cd {path}")

            # print to stdout so `eval` can evalute the command
            print(f"cd {path}", end='')

            # done!
            return
        else:
            tries += 1

    print_err(f"newdir tried and failed to create a directory {tries} times!")
    sys.exit(1)


if __name__ == "__main__":
    main()
