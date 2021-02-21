from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


def autolabel(ax,rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height/1e8),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("PySpark Demo") \
    .getOrCreate()

# 1.Tạo dataframe từ file NYSE.csv.
schema = StructType() \
    .add("MARKET", StringType(), True) \
    .add("TICKER", StringType(), True) \
    .add("DATE", DateType(), True) \
    .add("OPEN", DoubleType(), True) \
    .add("HIGH", DoubleType(), True) \
    .add("LOW", DoubleType(), True) \
    .add("CLOSE", DoubleType(), True) \
    .add("VOLUME", LongType(), True) \
    .add("FINAL", DoubleType(), True)

df = spark \
    .read \
    .option("header", "False") \
    .option("dateFormat", "yyyy-MM-dd") \
    .schema(schema) \
    .csv("D:/Pyspark/Data1/NYSE.csv")

df.printSchema()
df.show()
df.count()
# 2.Tính tổng số lượng giao dịch của từng cổ phiếu theo năm
# (Gồm các cột: năm, tên cổ phiếu, tổng số lượng giao dịch).
# Sắp thứ tự kết quả theo năm và tên cổ phiếu.
# .filter((col("year")>=2005) & (col("year")<=2010))
df1 = df.withColumn("year", year(col("date"))) \
    .filter(col("ticker")=="AEA") \
    .groupBy("year") \
    .agg(sum("volume").alias("total")) \
    .orderBy("year")
df1.show()

from matplotlib import pyplot as plt
import numpy as np

x = np.array(df1.select("year").collect()).reshape(-1)
y = np.array(df1.select("total").collect()).reshape(-1)
fig, ax=plt.subplots()
# reshape(-1): biến đổi array nhiều chiều thành array 1 chiều
bars =plt.bar(x,y,width = 0.75, color=np.random.rand(5,3))
autolabel(ax,bars)
plt.xticks(x,x,rotation=30)
#rotation=30:xoay 1 góc 30 độ
plt.xlabel("year")
plt.ylabel("total volume(100 million)")
plt.title('total volume by year of AEA')
plt.tight_layout()
plt.show()

spark.stop()