import numpy as np
import random
import time

import plotly.express as px


def kmeans(
  points: np.ndarray,
  k: int,
  max_iters: int = 100,
  distance_metric: callable = lambda x1, x2: np.linalg.norm(x1 - x2, ord=2, axis=-1)
):
  """Apply k-means clustering to `points`."""
  assert(max_iters >= 1)

  n, d = points.shape
  centroids = points[np.random.randint(0, n, size=(k,))]

  prev_nearest = None

  for _ in range(max_iters):
    # Step 1: Assign points to centroids.

    # distances = np.zeros((n, k))
    # for i in range(n):
    #   for j in range(k):
    #     distances[i][j] = distance_metric(points[i], centroids[j])

    distances = distance_metric(
      np.expand_dims(points, 1),
      np.expand_dims(centroids, 0)
    )

    nearest_clusters = np.argmin(distances, axis=-1) # shape (n,)

    # Stopping criterion: clusters have become stable.
    if prev_nearest is not None and (nearest_clusters == prev_nearest).all():
      break

    # Step 2: Re-calculate the centroids.
    for j in range(k):
      assigned_to_j = (nearest_clusters == j).nonzero()
      if len(assigned_to_j) > 0:
        centroids[j] = points[assigned_to_j].mean(axis=0)

    prev_nearest = nearest_clusters

  return nearest_clusters