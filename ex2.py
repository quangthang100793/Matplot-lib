from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import numpy as np

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("PySpark Demo") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

schema = StructType() \
    .add("id", IntegerType(), True) \
    .add("name", StringType(), True) \
    .add("gender", StringType(), True) \
    .add("age", IntegerType(), True) \
    .add("salary", LongType(), True)

df = spark \
    .read \
    .option("header", "True") \
    .schema(schema) \
    .csv("D:\Pyspark\Data1\emp.csvh")

df.show()
df.printSchema()
df.count

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(5)
x_labels = np.array(df.select("name").collect()).reshape(-1)
y = np.array(df.select("salary").collect()).reshape(-1)
#reshape(-1) biến đổi array nhiều chiều thành array 1 chiều

plt.bar(x,y,color = np.random.rand(5,3),width=.75)
# tra ve array 5 chieu 3 cot, tu do sẽ phân ra màu sắc theo chuỗi RGB
plt.xticks(x,x_labels,rotation=30) # quay 30 do 
plt.xlabel("employees")
plt.ylabel("salary")
plt.title('Salary')
plt.tight_layout()
plt.show()

spark.stop()