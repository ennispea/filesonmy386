"""
1. This parses the corpus files under corpus/in_all
2. ...
3. It dumps the prefixes into prefixes.json

"""


import sys
import json
import os
from collections import defaultdict

IN_DIR = "corpus/in_all"



def get_filenames():
    res = defaultdict(list)
    filenames = os.listdir(IN_DIR)

    for fn in filenames:
        print("processing:", fn)
        newres = dofile(os.path.join(IN_DIR, fn))
        for (k,v) in newres.items():
            res[k] += v
    print("processed %d files" % len(filenames))
    return res

def dofile(infile):
    lst = []
    prefixes = set()
    with open(infile) as r:
        for l in r:
            for word in l.split(","):
                try:
                    word = word.replace('"','')
                    word = word.replace('}','')
                    word = word.replace('{','')
                    word = word.strip()
                    prefix, suffix = word.split('.')

                    if '\\' in prefix:
                        continue

                    if len(prefix) > 8:
                        continue

                    # print prefix, suffix
                    lst.append("%s.%s" % (prefix, suffix))
                    prefixes.add(prefix)
                except:
                    # print "Error:", word
                    pass
    return {'filenames': lst,
            'prefixes': sorted(list(prefixes))}


def main(in_dir=None):
    result = get_filenames()
    n = result["filenames"]
    prefixes = result["prefixes"]
    # print("filenames", n)
    print("count:", len(n))
    print("prefix count:", len(prefixes))

    with open("prefixes.json", "w") as w:
        json.dump(dict(prefixes=prefixes), w)

    print("Done. HAve a nice Day!")

if __name__=="__main__":
    #main(sys.argv[1])
    main()
