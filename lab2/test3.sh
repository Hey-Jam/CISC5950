#!/usr/bin/bash
source ../env23.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../ParkingTicket.csv /part3/input/

for p in {2..5}
do
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 part3.py \
hdfs://$SPARK_MASTER:9000/part3/input/ $p
done

