from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("pyspark-sample").getOrCreate()

df = spark.read.csv("data/coursera_course_dataset_v2_no_null.csv", header=True, inferSchema=True)

df.printSchema()    # Prints the schema of the DataFrame
