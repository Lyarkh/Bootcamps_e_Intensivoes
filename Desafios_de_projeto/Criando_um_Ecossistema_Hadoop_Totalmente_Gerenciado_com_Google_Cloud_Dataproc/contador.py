import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark - Desafio Dataproc")
    words = sc.textFile("gs://desafio-dataproc/livro.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)
    wordCounts.saveAsTextFile("gs://desafio-dataproc/resultado.txt")
