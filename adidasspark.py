from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col

spark = SparkSession.builder.appName("adidas project").getOrCreate()

df = spark.read.csv(r"C:\Users\utkar\Downloads\adidas1.csv", header=True, inferSchema=True)

#df.show(5)

df = df.withColumn("Total Sales", regexp_replace(col("Total Sales"), ",", "").cast("double")) \
       .withColumn("operating profit", regexp_replace(col("operating profit"), ",", "").cast("double")) \
       .withColumn("price per unit", regexp_replace(col("price per unit"), ",", "").cast("double")) \
       .withColumn("units sold", regexp_replace(col("units sold"), ",", "").cast("double"))




# total_rows = df.count()
# distinct_rows = df.distinct().count()

# print("Total rows:", total_rows)
# print("Distinct rows:", distinct_rows)
# print("Duplicate rows:", total_rows - distinct_rows)

df.createOrReplaceTempView("ashok")

# spark.sql("select * from ashok").show()

# spark.sql("select sum(`Total Sales`) as total_sales,sum(`operating profit`) total_profit,avg(`price per unit`) av_price_per_unit,sum(`units sold`) total_unit_sold from ashok").show()

# spark.sql("""
#     SELECT 
#         SUM('Total Sales') AS total_sales,
#         SUM('operating profit') AS total_profit,
#         AVG('price per unit') AS av_price_per_unit,
#         SUM('units sold') AS total_unit_sold
#     FROM ashok
# """).show()

#2---total sales as per the month
# spark.sql("""
#     SELECT 
#     date_format(to_date(`Invoice Date`,'M/d/yyyy'),'MM') as months,
#     sum(`Total Sales`) as total_sales
#     FROM ashok
#     group by 1
# """).show()

#3.---total sales by state
# spark.sql("""select `state`,sum(`Total Sales`) from ashok
#           group by 1
#           """).show()

#4.---total sales by product
spark.sql("""select `Product`,sum(`Total Sales`) from ashok
          group by 1
          """).show()
          
# 5.Total sales by region
# spark.sql("""select `region`,sum(`Total Sales`) from ashok
#           group by 1
#           """).show()

#6.Total sales by retailer
# spark.sql("""select `Retailer`,sum(`Total Sales`) from ashok
#           group by 1
#           """).show()

# Units Sold by Product Category and Gender Type
spark.sql("""select `Retailer`,sum(`Total Sales`) from ashok
          group by 1
          """).show()

# Top Performing Cities by Profit
