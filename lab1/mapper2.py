#!/usr/bin/python
# --*-- coding:utf-8 --*--


import sys
from argparse import ArgumentParser
from collections import defaultdict

if __name__ == '__main__':

    # command line arguments
    parser=ArgumentParser()
    parser.add_argument('-s','--start',type=str,default=-1)
    parser.add_argument('-d','--delta',type=str,default=1)
    arg=parser.parse_args()

    if int(arg.start) < -1 or int(arg.start) > 23:
        raise ValueError('invalid start time: '+str(arg.start))

    if int(arg.delta) > 24 or int(arg.delta) <1 :
        raise ValueError('invalid time delta: '+str(arg.delta))


    if int(arg.start) == -1:
        for line in sys.stdin:
            line=line.strip()
            hour_ip,count=line.split()
            start,ip=hour_ip[1:6],hour_ip[7:]
            end=('0'+str(int(start[:2])+1))[-2:]+':00'
            print '%s\t%s' % ('['+start+'-'+end+']', ip+'['+count+']')


    else:
        end=min(int(arg.start)+int(arg.delta),24)
	start=('0'+str(arg.start))[-2:]
	end=('0'+str(end))[-2:]
	timeWindow='['+start+':00'+'-'+end+':00'+']'
	result=defaultdict(int)

        for line in sys.stdin:
            line=line.strip()

            if int(line[1:3]) >= int(arg.start) and int(line[1:3]) < int(end):
                hour_ip,count=line.split()
                ip=hour_ip[7:]
		count=int(count)
		result[timeWindow+ip]+=count
	
	for timeWindow_ip,num in result.items():
	    timeWindow,ip=timeWindow_ip[:13],timeWindow_ip[13:]
	    print '%s\t%s' % (timeWindow, ip+'['+str(num)+']')
