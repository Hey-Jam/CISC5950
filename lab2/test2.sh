#!/usr/bin/bash
source ../env23.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../ParkingTicket.csv /part2/input/

for k in {3..10}
do
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 part2.py \
hdfs://$SPARK_MASTER:9000/part2/input/ $k
done

