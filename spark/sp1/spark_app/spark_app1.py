from pyspark.sql import *

if __name__ == '__main__':
    spark = (
                SparkSession.builder 
                    .appName("LocalSparkApp")
                    .master("local[4]")
                    .getOrCreate()
    )

    numbers = [[1],[2],[3],[4],[5]]
    numbersDF = (
        spark
            .createDataFrame(numbers, "Id: int")
    )
    numbersDF.show()
    input('Press Enter To Continue')

