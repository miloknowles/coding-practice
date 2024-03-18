import numpy as np


def topological_sort(adj: np.array) -> list[int]:
  """Returns a topological sort of the nodes on `adj`, or returns `None` if there is a cycle.
  
  Basic idea:
  - Keep a "ready" set of nodes with no dependencies (incoming directed edges)
  - Remove a node from the "ready" set, and delete its outgoing edges from the graph
  - Add any neighbors that become "ready" (no incoming edges) are added to the ready set
  - Add the node the sorted output list
  """
  subgraph = adj.copy() # Don't modify original graph.

  ordering = []

  # Discover nodes with no dependencies. These are COLUMNS of all zeros in the
  # adjacency matrix.
  no_dependencies = np.argwhere(subgraph.sum(axis=0) == 0).flatten()

  ready = set(no_dependencies.tolist())

  while len(ready) > 0:
    u = ready.pop()
    vs = subgraph[u].nonzero()[0]

    # Delete outgoing edges from u.
    for v in vs:
      subgraph[u, v] = 0

      # If v has no incoming edges, add to the ready set.
      if subgraph[:,v].sum() == 0:
        ready.add(v)

    ordering.append(u)

  # If the ordering does not contain all nodes at this point, there must
  # have been a cycle that prevented a node from becoming ready.
  if len(ordering) < len(subgraph):
    return None

  return ordering


if __name__ == "__main__":
  # Make an example graph:
  A = np.zeros((6, 6))
  # A[u,v] = 1 indicates that there is a directed edge FROM u TO v.
  A[0, 2] = 1
  A[1, 2] = 1
  A[2, 5] = 1
  A[2, 3] = 1
  A[3, 4] = 1
  A[5, 3] = 1

  ordering = topological_sort(A)
  print(ordering) # 0, 1, 2, 5, 3, 4

  # Make an example with a cycle:
  A = np.zeros((6, 6))
  # A[u,v] = 1 indicates that there is a directed edge FROM u TO v.
  A[0, 2] = 1
  A[1, 2] = 1
  A[2, 5] = 1
  A[2, 3] = 1
  A[3, 2] = 1 # <-- creates cycle!
  A[3, 4] = 1

  ordering = topological_sort(A)
  print(ordering)