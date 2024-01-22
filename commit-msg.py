#!/usr/bin/env python3

import sys
import re

rules = """
# You didn't follow the git commit message rules!
"""

keys = "|".join(["DAZWVS", "DMBA"])
prompts = "|".join(["Fix", "Add", "Expand", "Chore", "Remove", "Stop", "Start", "Contract", "Doc", "Tweak", "Optimize"])
forbidden = "".join([".", ","])

# ^(DAZWVS|DMBA)-(\d{4,5})\s(Add|Fix)\s[^.,]*$
pattern = "^(" + keys + ")-(\d{4,5})\s(" + prompts + ")\s[^" + forbidden + "]*$"

def main():
	with open(sys.argv[1], "r") as fp:
		lines = fp.readlines()

		for idx, line in enumerate(lines):

			if line.strip() == "# ------------------------ >8 ------------------------":
				break

			if line[0] == "#":
				continue

			if not line_valid(idx, line):
				print(rules)
				sys.exit(1)

	sys.exit(0)

def line_valid(idx, line):
	if idx == 0:
		return re.match(pattern, line)
	elif idx == 1:
		return len(line.strip()) == 0
	else:
		return len(line.strip()) <= 72

if __name__ == "__main__":
	main()