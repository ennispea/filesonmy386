import sys
import json
import os

IN_DIR = "corpus/in_all"

def get_filenames():
    res = []
    filenames = os.listdir(IN_DIR)

    for fn in filenames:
        res = res + dofile(os.path.join(IN_DIR, fn))
    return res

def dofile(infile):
    lst = []
    with open(infile) as r:
        for l in r:
            for word in l.split(","):
                try:
                    word = word.replace('"','')
                    word = word.replace('}','')
                    word = word.replace('{','')
                    word = word.strip()
                    prefix, suffix = word.split('.')
                    # print prefix, suffix
                    lst.append("%s.%s" % (prefix, suffix))
                except:
                    # print "Error:", word
                    pass
    return lst

def main(in_dir=None):
    n = get_filenames()
    print(n)
    print(len(n))

if __name__=="__main__":
    #main(sys.argv[1])
    main()
