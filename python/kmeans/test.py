from .kmeans import *

# Set up the input data:
d = 2 # the dimensionality of each data point
n = 1000 # the number of points
c = 10

# Randomly generate some clusters:
data = []
for _ in range(c):
  scale = 0.3
  offset = np.random.random(d)
  cluster = scale * np.random.random((n // c, d)) + offset
  data.append(cluster)

points = np.concatenate(data)

t0 = time.time()
out = kmeans(points, c, max_iters=100)

elapsed = time.time() - t0
print(f"elapsed: {elapsed:.3f}")

out
fig = px.scatter(x=points[:,0], y=points[:,1], color=out)
fig.show()