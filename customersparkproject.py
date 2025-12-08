from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("customer and other 4 csv").getOrCreate()
from pyspark.sql.functions import col,sum
#1.read all 5 files
customer_df=spark.read.csv(r"e:\sparkpproject\customer",header=True,inferSchema=True)
product_df=spark.read.csv(r"e:\sparkpproject\product",header=True,inferSchema=True)
people_df=spark.read.csv(r"e:\sparkpproject\people",header=True,inferSchema=True)
orgnization_df=spark.read.csv(r"e:\sparkpproject\orgnization",header=True,inferSchema=True)
lead_df=spark.read.csv(r"e:\sparkpproject\lead",header=True,inferSchema=True)

#2.dispaly th all 5files content
# customer_df.show(1)
# people_df.show(1)
# lead_df.show(1)
# product_df.show(1)
# orgnization_df.show(1)

#3.check schema
# customer_df.printSchema()
# people_df.printSchema()
# lead_df.printSchema()
# product_df.printSchema()
# orgnization_df.printSchema()

#4.check count of row
# print(customer_df.count())
# print(lead_df.count())
# print(product_df.count())
# print(product_df.count())
# print(orgnization_df.count())

#5.Find null values
customer_df.select([sum(col(c).isNull().cast("int")).alias(c) for c in customer_df.columns]).show()
lead_df.select([sum(col(c).isNull().cast("int")).alias(c) for c in lead_df.columns]).show()
orgnization_df.select([sum(col(c).isNull().cast("int")).alias(c) for c in orgnization_df.columns]).show()

orgnization_df=orgnization_df.fillna({"Number of employees":100,
                      "Industry":"komal",
                      "Name":"shinde"})
orgnization_df.select([sum(col(c).isNull().cast("int")).alias(c) for c in orgnization_df.columns]).show()
lead_df.select([sum(col("xyz").isNull().cast()).alias("")])