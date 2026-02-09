#!/usr/bin/env python3
import os
import datetime as dt

name = os.getenv("INPUT_WHO_TO_GREET", "World")

## Alternatively pass input as argument
# name = sys.argv[1] if len(sys.argv) > 1 else "World"


greeting = f"Hello, {name}! Time is {dt.datetime.now(dt.timezone.utc):%H:%M:%S} UTC."
print(greeting)

print(f"::notice file=entrypoint.py,line=12::{greeting}")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"greeting={greeting}\n")