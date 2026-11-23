from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Test") \
    .getOrCreate()

df = spark.read.parquet(r"C:\Github\chess-spark-compatible")

df.show(1,truncate=False)