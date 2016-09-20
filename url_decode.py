#!/usr/bin/env python
#-*- coding = 'utf-8'-*-

import sys
import urllib2

def urldecode(s):
    return urllib2.unquote(s).decode('utf8').strip()

for line in sys.stdin:
    print urldecode(line)
