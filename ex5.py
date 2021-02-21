from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects: # vong lap
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height/1e8),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# ha la canh giua theo chieu ngang, va la canh giua theo chieu doc

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
# 2.Tính tổng số lượng giao dịch của từng cổ phiếu theo năm
# (Gồm các cột: năm, tên cổ phiếu, tổng số lượng giao dịch).
# Sắp thứ tự kết quả theo năm và tên cổ phiếu.
# .filter((col("year")>=2005) & (col("year")<=2010))

df1 = df.withColumn("year", year(col("date"))) \
    .filter((col("ticker").isin(["AEA","AKP"])) & (col("year").between(2004,2010))) \
    .groupBy("year","ticker") \
    .agg(sum("volume").alias("total")) \
    .orderBy("year","ticker")
df1.show()
#quit()

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(11)
x_labels = np.array(df1.select("year").collect()).reshape(-1)
y = np.array(df1.select("total").collect()).reshape(-1)

fig, ax = plt.subplots()
bars = plt.bar(x,y,color=np.random.rand(11,3),width=.5)
autolabel(ax,bars)

plt.xticks(x,x_labels,rotation=30) # quay 30 do
plt.xlabel("years")
plt.ylabel("Total Volume (100 millions)")
plt.title('Total Volume by Years of AEA')
plt.tight_layout()
plt.show()

