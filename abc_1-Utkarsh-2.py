from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("WindowFunctionsExample").getOrCreate()
data = [
    ("A", "2023-01-01", 100),
    ("A", "2023-01-02", 200),
    ("A", "2023-01-03", 300),
    ("B", "2023-01-01", 400),
    ("B", "2023-01-02", 500),
    ("B", "2023-01-03", 600),
    ("C", "2023-01-01", 700),
    ("C", "2023-01-02", 800),
    ("C", "2023-01-03", 900),
]

df = spark.createDataFrame(data, ["Category", "Date", "Sales"])
df.show()