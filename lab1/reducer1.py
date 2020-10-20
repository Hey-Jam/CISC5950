#!/usr/bin/python
# --*-- coding:utf-8 --*--

from collections import defaultdict
import sys

if __name__ == '__main__':

    result=defaultdict(int)

    for line in sys.stdin:
        line=line.strip()
        hour_ip, num=line.split()
        try:
            result[hour_ip] += int(num)

        except Exception as e:
            pass


    sorted_result=sorted(result.items(), key=lambda x: x[1], reverse=True)

    for hour_ip, count in sorted_result:
        print '%s\t%s' % (hour_ip,count)
