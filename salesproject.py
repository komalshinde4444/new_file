from pyspark.sql import SparkSession
from pyspark.sql.functions import col,  sum as _sum , avg

#---spark session initialize and read data
spark=SparkSession.builder.appName("Sales Mini Project").getOrCreate()
df=spark.read.csv("E:\DataEnggFiles\sales.csv",header=True, inferSchema=True)
df.show()

#----operations
# df.printSchema()
# df.select("region").show() #------show particular column
# print(df.count()) #---calculate total count
# print(df.first())  #------show first record

#print null values count
df.select([_sum(col(c).isNull().cast("int")).alias(c) for c in df.columns]).show()

