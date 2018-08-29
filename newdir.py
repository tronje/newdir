#!/usr/bin/env python3

import os
import random
import sys
import tempfile

from animals import animals
from adjectives import adjectives


while True:
    try:
        adjective = random.choice(adjectives)
        animal = random.choice(animals)

        dirname = adjective + '_' + animal
        dirpath = os.path.join(tempfile.gettempdir(), dirname)

        os.mkdir(dirpath)
        break
    except FileExistsError:  # directory exists already
        if len(animals) > len(adjectives):
            animals.remove(animal)
        else:
            adjectives.remove(adjective)
    except IndexError:  # no animals or adjectives left
        print(
            "newdir exhausted all choices!",
            file=sys.stderr
        )
        sys.exit(1)
    except Exception as e:
        print(f"newdir failed with '{type(e)}: {e}'", file=sys.stderr)
        sys.exit(1)

print(f"cd {dirpath}", file=sys.stderr)
print(f"cd {dirpath}", end='')
