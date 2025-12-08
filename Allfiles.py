from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("MySQL_Read") \
      .getOrCreate()  
sc=spark.sparkContext

# data_csv=spark.read.csv(r"E:\DataEnggFiles\Match_Data.csv",header=True,inferSchema=True)
# data.show()

# data_text=spark.read.option("delimiter",",").csv(r"E:\DataEnggFiles\Match_Data.txt",header=True,inferSchema=True)
# data_text.show()

# data_paraq=spark.read.parquet(r"E:\DataEnggFiles\weather.parquet",header=True,inferSchema=True)
# data_paraq.show()

# data_orc=spark.read.orc(r"E:\DataEnggFiles\part-00005-5df36169-249c-4e9f-9d3f-8c02a0aa303f-c000.snappy.orc")
# data_orc.show()

data_json=spark.read.option("multiline",True).json("E:\DataEnggFiles\house-price-parquet.json")
data_json.show()