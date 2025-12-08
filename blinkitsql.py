from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("blinkit_sql").getOrCreate()
df=spark.read.option('delimiter',',').csv(r"E:\DataEnggFiles\blinkit.txt",header=True, inferSchema=True)
# df.show(5)
df.createOrReplaceTempView("blinkit")

#1️⃣ View all data:
# spark.sql("""
#           select * from blinkit limit 5
#           """).show()

#2️⃣ Show only first 10 rows:
# spark.sql("""
#           select * from blinkit limit 10
#           """).show()

#3️⃣ Get unique payment methods
# spark.sql("""
#           select distinct payment_method from blinkit 
#           """).show()

#4️⃣ Count total number of orders
# spark.sql("""
#           select count(*) from blinkit 
#           """).show()

#5️⃣ List all orders that are delivered
# spark.sql("""select * from blinkit where delivery_status='On Time' """).show()

#6️⃣ Find all orders with total > 1000
# spark.sql("""
#           select * from blinkit where order_total>1000
#           """).show()

#7️⃣ Count orders by each delivery status
# spark.sql("""
#           select delivery_status,count(*) from blinkit group by delivery_status
#           """).show()

#8️⃣ Calculate total revenue by payment method
# spark.sql("""
#           select payment_method,sum(order_total) from blinkit group by payment_method
#           """).show()

#9️⃣ Find average order value (AOV) per store
# spark.sql("""
#           select store_id ,avg(order_total) as all from blinkit group by store_id order by all 
#           """).show()

#🔟 Get total orders handled by each delivery partner
# spark.sql("""select delivery_partner_id,
#           count(order_id) as all_order from blinkit
#           group by delivery_partner_id order by all_order desc """).show()


#🔵 3️⃣ Advanced SQL Queries
#1️⃣ Find top 5 customers by total spending
# spark.sql("""
#           select customer_id,round(sum(order_total),2) from blinkit group by customer_id order by count(*) desc limit 5  
#           """).show()

#2️⃣ Calculate delivery delay (actual vs promised)
# spark.sql("""
#           select order_id
#           , datediff(actual_delivery_time,promised_delivery_time) as diff_actual_promised from blinkit
#           """).show()

#3️⃣ Find average delay by delivery partner
# spark.sql("""
#           select delivery_partner_id
#           , avg(datediff(actual_delivery_time,promised_delivery_time)) as diff_actual_promised from blinkit group by delivery_partner_id
#           """).show()

#4️⃣ Find revenue by day
spark.sql("""
          select day(order_date) as all,sum(order_total) from blinkit
          group by all 
          order by all desc
          """).show()
