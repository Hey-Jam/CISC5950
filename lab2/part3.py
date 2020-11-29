from __future__ import print_function
import sys
from pyspark.sql import SparkSession
from operator import add

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Wrong arguments number')
        sys.exit(-1)

    spark=SparkSession.builder.appName('Part3').getOrCreate()
    dates=spark.read.csv(sys.argv[1], inferSchema=True, header=True)\
                .select('Issue Date').collect()

    parallelization=sys.argv[2]

    dateCountsRdd=spark.sparkContext.parallelize(dates,parallelization)\
                            .map(lambda x: (x,1)).reduceByKey(add)

    dateCounts=dateCountsRdd.collect()

    output=sorted(dateCounts, key=lambda x: x[1], reverse=True)[0]

    print('parallelization='+str(p)+':', output[0],output[1])

    spark.stop()