"""
Generate extensions.json

To run:
python extensions.py

"""

import json

def generate_extensions():
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

    print("Generated extensions.json")
    return res

if __name__ == '__main__':
    res = generate_extensions()
    with open("extensions.json", "w") as w:
        json.dump(dict(extension=res), w, sort_keys=True)
