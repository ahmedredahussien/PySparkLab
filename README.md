# PySparkLab

1. Download Spark 
https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
 Reference : https://spark.apache.org/downloads.html
 
2. Download winutils
https://github.com/steveloughran/winutils/blob/master/hadoop-3.0.0/bin/winutils.exe
Reference : https://github.com/steveloughran/winutils 


3. JDK download 
https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.exe
Reference : https://www.oracle.com/java/technologies/downloads/

* Extract download spark zip folder
* Install all the previous

---

1. Create a folder called hadoop under c:/Hadoop/bin and place winutils.exe inside it

2. Add new System variable under Enviroment variable 
* HADOOP_HOME=c:/Hadoop
* SPARK_HOME=<Path to extracted  spark folder>
* JAVA_HOME=C:\Program Files\Java\jdk-11.0.17

Update *path* variable to include the bin diretories 
* %JAVA_HOME%\bin
* %SPARK_HOME%\bin
* %HADOOP_HOME%\bin

3. Go to spark-3.5.0-bin-hadoop3\python\lib

py4j-0.10.9.7-src.zip
Update the path System environment variable with - the absolute path of the py4j-0.10.9.7-src.zip, i.e. <your local path location>\spark-3.5.0-bin-hadoop3\python\lib\py4j-0.10.9.7-src.zip

4. test spark command using "cmd" command prompt
spark-submit --version

5. Add content root in Project Structure under pycharm settings

Point to both libs
* py4j-0.10.9.7-src.zip
* pyspark.zip

Sample pyspark code
bash 
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("pyspark-sample").getOrCreate()

df = spark.read.csv("data/coursera_course_dataset_v2_no_null.csv", header=True, inferSchema=True)

df.printSchema()
```
