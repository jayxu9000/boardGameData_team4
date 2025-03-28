# Cleaning - filling in missing values w/ 0's
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

from pyspark.sql import Window
from pyspark.sql.functions import row_number

spark = SparkSession.builder.appName("BoardGamesETL").getOrCreate()

primary_input = "/opt/spark/files/in/boardgames_ranks.csv" 
secondary_input = "/opt/spark/files/in/BGG_Data_Set.csv" 
output_path = "/opt/spark/files/out/csv"  

primary_df = spark.read.csv(primary_input, header=True, inferSchema=True)
secondary_df = spark.read.csv(secondary_input, header=True, inferSchema=True)

merged_df = primary_df.join(secondary_df, on=["bgg_id", "boardgame_name", "users_rated", "year_published"], how="left")

# merged_df.write.csv(output_path, header=True, mode="overwrite")

# rename_part_to_file_name(output_path, "finalboardgame.csv")

valid_df = merged_df.filter(
    when(col('year_published').cast('integer').isNotNull(), True)  # Valid cast
    .otherwise(col('year_published').isNull())                         # Keep nulls (optional)
)

valid_df = valid_df.fillna(0)

# Add sequential IDs ordered by a unique column (e.g., bgg_id)
window = Window.orderBy("bgg_id")  # Use a unique column for ordering
valid_df = valid_df.withColumn("boardgame_id", row_number().over(window))

newPrimary_df = valid_df.select(
    "boardgame_id",
    "bgg_id",
    "boardgame_name",
    "users_rated",
    "year_published",
    "bayes_average",
    "average",
    "is_expansion",
    "min_players",
    "max_players",
    "play_time",
    "min_age",
    "rating_average",
    "complexity_average",
    "owned_users"
)

rank_df = valid_df.select(
    "boardgame_id",
    "boardgame_rank",
    "abstracts_rank",
    "cgs_rank",
    "childrensgames_rank",
    "familygames_rank",
    "partygames_rank",
    "strategygames_rank",
    "thematic_rank",
    "wargames_rank",
    "bgg_rank"
)

jdbc_options = {
    "url": spark.conf.get("spark.mysql.boardgame.url"),
    "user": spark.conf.get("spark.mysql.boardgame.user"),
    "password": spark.conf.get("spark.mysql.boardgame.password"),
    "driver": "com.mysql.cj.jdbc.Driver",
}

newPrimary_df.write.format("jdbc").options(**jdbc_options, dbtable="boardgame_primary").mode(
    "append"
).save()

rank_df.write.format("jdbc").options(**jdbc_options, dbtable="boardgame_rank").mode(
    "append"
).save()

spark.stop()

# done 3/28/2025 6:36 PM