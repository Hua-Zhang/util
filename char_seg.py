#!/usr/bin/env python
#-*-coding = utf-8-*-
# split line into char list
import sys

def charseg(str):
        str = unicode(str,"utf-8")
        l = list(str)
        m = ""
        for i in range(len(l)):
                if m != "":
                        m = m + " " + l[i]
                else:
                        m = l[i]
        return m.encode("utf-8")

for line in sys.stdin:
        segresult = charseg(line.strip())
        print segresult
