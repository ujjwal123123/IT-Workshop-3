import sys
import numpy as np
from math import sqrt

from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans

DATA_SOURCE_URI = "s3://ujjwal-assignment-9/adult.csv"
DATA_OUTPUT_URI = "s3://ujjwal-assignment-9/output/"


if __name__ == "__main__":
    sc = SparkContext(appName="KMeansExample")

    # data = sc.textFile("hdfs://localhost:9000/spark-kmeans/adultdata.txt")
    data = sc.textFile(DATA_SOURCE_URI)
    parsedData = data.map(
        lambda line: np.array([x for x in line.split(", ")])[
            np.array([0, 2, 11])
        ].astype(float)
    )

    # Build the model (cluster the data)
    clusters = KMeans.train(
        parsedData, 2, maxIterations=20, initializationMode="random"
    )
    cluster_center = clusters.centers
    print("Centers:", clusters.centers, file=sys.stdout)

    # Evaluate clustering by computing Within Set Sum of Squared Errors
    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x ** 2 for x in (point - center)]))

    sc.stop()
