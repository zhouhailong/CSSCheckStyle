#/usr/bin/python
#encoding=utf-8
from BinaryRule import *
import re

# http://www.swordair.com/tools/css-hack-table/
# big table

# some hacks
RULE_HACKS = [
    [r'^_',                     1,  IE6],
    [r'^\+',                    1,  IE6 | IE7],
    [r'^\*',                    1,  IE6 | IE7],
    [r'\\9',                    2,  ALLIE],
    [r'\\0/',                   2,  IE8],
    [r'\\0',                    2,  IE8 | IE9PLUS],
    [r'zoom|behavior|filter',   1,  ALLIE],
    [r'expression',             2,  ALLIE],
    [r'^\-webkit\-',            1,  WEBKIT],
    [r'^\-moz\-',               1,  FIREFOX],
    [r'^\-ms\-',                1,  IE9PLUS],
    [r'^\-khtml\-',             1,  ALLIE],
    [r'^\-o\-',                 1,  OPERA]
]

# some hacks
RULESET_HACKS = [
    [r'\*html',                 IE6],
    [r'\*\+html',               IE7],
    [r'\*:first\-child\+html',  IE7],
    [r'html>body',              IE7 | IE8 | IE9PLUS],
    [r'html>/\*\*/body',        IE8 | IE9PLUS]
]

def doRuleDetect(name, value):
    for hack in RULE_HACKS:
        pattern = re.compile(hack[0])
        match = pattern.match(name if hack[1] == 1 else value)
        if match:
            return hack[2]
    return STD

def doRuleSetDetect(selector):
    for hack in RULESET_HACKS:
        pattern = re.compile(hack[0])
        match = pattern.match(selector)
        if match:
            return hack[1]
    return STD

if __name__ == '__main__':
    print doRuleDetect('-moz-fdafda', 'fda') & (IE6 | STD)