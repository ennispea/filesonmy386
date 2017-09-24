"""
Generate extensions.json

To run:
python extensions.py

"""

import json

res = []

with open("Extensions.source") as r:
    for line in r:
        line = line.strip()
        parts = line.split(":")
        print(parts)
        if len(parts)==2:
            try:
                reps = int(parts[1])
            except:
                print("Can't parse number: %s" % parts[1])
                reps = 1
        else:
            reps = 1

        for i in range(reps):
            res.append(parts[0])

with open("extensions.json", "w") as w:
    json.dump(dict(extensions=res), w, sort_keys=True)

print("Generated extensions.json")
