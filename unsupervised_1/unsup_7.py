# Import Normalizer
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from unsupervised_1.unsup_c3 import movements
import numpy as np
import pandas as pd

from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)
