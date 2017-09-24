import sys
import json
import os

def read_dirs(filename):
    with open(filename) as r:
        dirs = set(l.strip().upper() for l in r)
    return sorted(dirs)

def main():
    dir1 = read_dirs("DIR1")
    dir2 = read_dirs("DIR2")

    with open("dir1.json", "w") as w:
        json.dump(dict(dir1=dir1, dir2=dir2), w, sort_keys=True)

if __name__=="__main__":
    # main(sys.argv[1])
    main()
