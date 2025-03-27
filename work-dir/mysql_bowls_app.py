from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("BowlsApp").getOrCreate()

jdbc_options = {
    "url": spark.conf.get("spark.mysql.bowls.url"),
    "user": spark.conf.get("spark.mysql.bowls.user"),
    "password": spark.conf.get("spark.mysql.bowls.password"),
    "driver": "com.mysql.cj.jdbc.Driver",
}

# select directly from the item table
item_df = spark.read.format("jdbc").options(**jdbc_options, dbtable="item").load()

# select from a query,
# an alias IS required
sql = """
(SELECT
    o.order_id,
    o.order_date,
    o.customer_id,
    o.order_status_id,
    oi.order_item_id,
    oi.item_id,
    oi.quantity,
    oi.notes
FROM `order` o
INNER JOIN order_item oi ON o.order_id = oi.order_id) AS order_item
"""

order_item_df = spark.read.format("jdbc").options(**jdbc_options, dbtable=sql).load()

# merge and load to CSV
total_df = order_item_df.join(item_df, on="item_id").drop("item_id")
total_df = total_df.drop("customer_id", "notes", "description")

total_df.write.csv("/opt/spark/files/out/csv/bowls", header=True, mode="overwrite")

# insert into the item table
new_item_df = spark.createDataFrame(
    [
        ("Jelly Beans", "Not spiced jelly beans, fruity", 3.99),
        ("Nerds Gummy Clusters", "Yum :)", 4.98),
    ],
    schema=["name", "description", "price"],
)

new_item_df.write.format("jdbc").options(**jdbc_options, dbtable="item").mode(
    "append"
).save()


spark.stop()
