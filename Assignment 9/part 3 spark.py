from pyspark.context import SparkContext
from pyspark.mllib.clustering import KMeans
import numpy as np
import sys


DATA_SOURCE_URI = "s3://expsecondbucket/adultdata.txt"
DATA_OUTPUT_URI = "s3://ujjwal-assignment-9/output/"


def solve(data_source: str, output_uri: str):
    """
    :param data_source
    :param output_uri
    """

    with SparkContext(appName="KMeans") as sc:
        data = sc.textFile("./adult.csv")
        parsedData = data.map(
            lambda line: np.array([x for x in line.split(", ")])[
                np.array([0, 2, 11])
            ].astype(float)
        )

        # Build the model (cluster the data)
        clusters = KMeans.train(parsedData, 2)
        output = clusters.centers

        # save the output
        print(clusters.centers, clusters, file=sys.stdout)


if __name__ == "__main__":
    solve(DATA_SOURCE_URI, DATA_OUTPUT_URI)
