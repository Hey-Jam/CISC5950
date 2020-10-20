#!/bin/sh

show_usage="args: [-s -d -t]"

start="-1"
delta="1"
top="0"

while getopts ":s:d:t:" opt
do
    case $opt in
	s)
	start=$OPTARG
	;;
	d)
	delta=$OPTARG
	;;
	t)
	top=$OPTARG
	;;
	?)
	echo "invalid option";
	echo $show_usage;
	exit;;
    esac
done


../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /assignment/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /assignment/output1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /assignment/output2/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /assignment/input/

# copy log data to HDFS
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /assignment/input/

# First round of MapReduce using Hadoop Streaming
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/assignment/mapper1.py -mapper mapper1.py \
-file ../../mapreduce-test-python/assignment/reducer1.py -reducer reducer1.py \
-input /assignment/input/* -output /assignment/output1/

# Second round of MapReduce using Hadoop Streaming
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/assignment/mapper2.py -mapper "python mapper2.py -s $start -d $delta" \
-file ../../mapreduce-test-python/assignment/reducer2.py -reducer "python reducer2.py -t $top" \
-input /assignment/output1/* -output /assignment/output2/

/usr/local/hadoop/bin/hdfs dfs -cat /assignment/output2/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /assignment/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /assignment/output1/
/usr/local/hadoop/bin/hdfs dfs -rm -r /assignment/output2/
../../stop.sh
