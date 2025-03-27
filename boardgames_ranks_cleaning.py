# Cleaning - filling in missing values w/ 0's

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

spark = SparkSession.builder.appName("BoardGamesETL").getOrCreate()

input_path = "file_path_here"  
output_path = "file_path_here"  

df = spark.read.csv(input_path, header=True, inferSchema=True)

df_filled = df.fillna(0)

df_filled.write.csv(output_path, header=True, mode="overwrite")

spark.stop()


