from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("CourseProcessing").getOrCreate()

# Assuming 'your_dataset.csv' is the name of your dataset file
# You need to replace it with the actual path to your dataset
dataset_path = "data/coursera_course_dataset_v2_no_null.csv"

# Read the dataset into a DataFrame
df = spark.read.csv(dataset_path, header=True, inferSchema=True)

# Show the initial structure of the DataFrame
df.printSchema()

# Display the first few rows of the DataFrame
df.show(5, truncate=False)

# Example: Extract skills from the 'Skills' column
# Note: You may need to adjust this depending on the actual structure of your data
skills_df = df.select('Title', 'Organization', 'Skills')

# Example: Filter courses with ratings greater than a certain threshold
highly_rated_courses = df.filter(col('Ratings') >= 4.0)

# Example: Compute average ratings for each organization
avg_ratings_by_org = df.groupBy('Organization').agg({'Ratings': 'avg'}).withColumnRenamed('avg(Ratings)', 'AvgRatings')

# You can perform similar operations for other columns as needed

# Show the final structure of the DataFrame after processing
skills_df.printSchema()

# Display the results
skills_df.show(5, truncate=False)
highly_rated_courses.show(5, truncate=False)
avg_ratings_by_org.show(truncate=False)

# Stop the Spark session
spark.stop()
