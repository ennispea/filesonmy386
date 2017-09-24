import sys
import json
import os

def main():
    os.list

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

    print json.dumps(lst)
if __name__=="__main__":
    main(sys.argv[1])
