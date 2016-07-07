#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=Fogbugz:%2012345&3

import re
import sys

txt='Fogbugz: 12345'

re1='.*?'	# Non-greedy match on filler
re2='(\\d+)'	# Integer Number 1

rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    int1=m.group(1)
    print int1