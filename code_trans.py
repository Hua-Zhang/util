#!/usr/bin/env python
#-*-coding = utf-8-*-
#A character encoding conversion
import sys

text_type = unicode

def strdecode(sentence):
        if not isinstance(sentence, text_type):
                try:
                        sentence = sentence.decode('utf-8')
                except UnicodeDecodeError:
                        sentence = sentence.decode('gbk', 'ignore')
                return sentence

for line in sys.stdin:
        trans = strdecode(line).strip()
        print trans.encode("utf-8")
