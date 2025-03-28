from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FirstPySparkApp").getOrCreate()

print(spark)
print("Hello from first PySpark app!")

spark.stop()
