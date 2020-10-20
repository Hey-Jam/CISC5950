#!/usr/bin/python
# --*-- coding:utf-8 --*--

import re
import sys

if __name__ == '__main__':

    patterm=re.compile('(?P<ip>\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?')

    for line in sys.stdin:
        match=patterm.search(line)

        if match:
	    if int(match.group('hour')) <= 23 and int(match.group('hour')) >= 0:
                print '%s\t%s' % ('['+match.group('hour')+':00'+']'+match.group('ip'),1)
