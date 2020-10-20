#!/usr/bin/python
# --*-- coding:utf-8 --*--

import sys
from argparse import ArgumentParser

if __name__ == '__main__':
    parser=ArgumentParser()
    parser.add_argument('-t','--top',type=str,default=0)
    arg=parser.parse_args()

    if int(arg.top) < 0:
        raise ValueError('invalid value for option top: '+str(arg.top))

    result={}

    for line in sys.stdin:
        line=line.strip()
        timeWindow, ip_count=line.split()
        ip,count=ip_count.split('[')
        count=int(count[:-1])

        try:
            result[timeWindow].append((ip,count))

        except KeyError:
            result[timeWindow]=[]
            result[timeWindow].append((ip,count))

    time_sorted_result=sorted(result.items(), key=lambda x: x[0][1:3])

    for timeWindow, ip_count in time_sorted_result:
        sorted_result=sorted(ip_count, key=lambda x: x[1], reverse=True)

        if int(arg.top) == 0:
            for ip,count in sorted_result:
                print '%s\t%s' % (timeWindow+ip, count)

        else:
            for ip,count in sorted_result[:int(arg.top)]:
                print '%s\t%s' % (timeWindow+ip, count)

