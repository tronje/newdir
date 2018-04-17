#!/usr/bin/env python3

import os
import random
import subprocess


adjectives = [
    "acidic",
    "bald",
    "bitter",
    "brave",
    "calm",
    "chubby",
    "clean",
    "cool",
    "creamy",
    "drab",
    "eager",
    "fancy",
    "fit",
    "flabby",
    "fresh",
    "gentle",
    "greasy",
    "happy",
    "hot",
    "jolly",
    "juicy",
    "kind",
    "lively",
    "long",
    "moldy",
    "nice",
    "nutty",
    "plain",
    "plump",
    "polite",
    "proud",
    "putrid",
    "quaint",
    "rancid",
    "ripe",
    "rotten",
    "salty",
    "savory",
    "short",
    "silly",
    "skinny",
    "sour",
    "spicy",
    "stale",
    "stocky",
    "sweet",
    "tangy",
    "tart",
    "tasty",
    "ugly",
    "witty",
    "yummy",
    ]

animals = [
    "alpaca",
    "ant",
    "ape",
    "donky",
    "baboon",
    "badger",
    "bat",
    "bear",
    "beaver",
    "bee",
    "beetle",
    "bug",
    "bull",
    "camel",
    "cat",
    "cicada",
    "clam",
    "cod",
    "coyote",
    "crab",
    "crow",
    "deer",
    "dog",
    "duck",
    "eel",
    "elk",
    "ferret",
    "fish",
    "fly",
    "fox",
    "frog",
    "gerbil",
    "gnat",
    "gnu",
    "goat",
    "hare",
    "hornet",
    "horse",
    "hound",
    "hyena",
    "impala",
    "jackal",
    "koala",
    "lion",
    "lizard",
    "llama",
    "locust",
    "louse",
    "mole",
    "monkey",
    "moose",
    "mouse",
    "mule",
    "otter",
    "ox",
    "oyster",
    "panda",
    "pig",
    "pug",
    "rabbit",
    "salmon",
    "seal",
    "shark",
    "sheep",
    "skunk",
    "snail",
    "snake",
    "spider",
    "swan",
    "tiger",
    "trout",
    "turtle",
    "walrus",
    "wasp",
    "weasel",
    "whale",
    "wolf",
    "wombat",
    "worm",
    "yak",
    "zebra",
]


if __name__ == "__main__":
    s_adj = sorted(adjectives)

    print("adjectives = [")
    for item in s_adj:
        print(f'    "{item}",')
    print("]")

    raise Exception("lol")

    whoami = subprocess.check_output(["whoami"])
    whoami = whoami.decode("utf-8")
    whoami = whoami.strip()

    tmpdir = os.path.join("/tmp", whoami)

    while True:
        adjective = random.choice(adjectives)
        animal = random.choice(animals)

        dirname = adjective + '_' + animal
        dirpath = os.path.join(tmpdir, dirname)

        try:
            os.mkdir(dirpath)
            break
        except FileExistsError:
            pass

    print(f"cd {dirpath}", end='')
