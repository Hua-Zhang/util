#!/usr/bin/env python
#-*- coding:UTF-8 -*-
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

def trans(out_code):
    for line in sys.stdin:
        trans = strdecode(line).strip("\n")
        # out_code("utf-8" || 'gbk')
        print trans.encode(out_code)

if __name__=="__main__":
    out_code = "utf-8"
    if len(sys.argv) == 2:
        if sys.argv[1].strip() == "-h":
            print "Usage: code_trans out_code(utf-8||gbk||..., default=utf-8)"
            exit(1)
        out_code = sys.argv[1].strip()
    trans(out_code)
