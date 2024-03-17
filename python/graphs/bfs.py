from collections import deque


def bfs(graph: dict[str, list[str]], node: str):
  """Breadth-first search of graph, starting from node."""
  # Keep track of nodes visited so far (to prevent cycles). Nodes
  # are considered visited when added to the queue.
  visited = {node}

  sequence = []

  # Maintain a queue of nodes to visit next.
  queue = deque([node])

  while len(queue) > 0:
    current = queue.popleft()
    sequence.append(current)

    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append(neighbor)
        visited.add(neighbor)

  return sequence


# Defines node adjacency
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : ['9'],
  '9': []
}

bfs(graph, '5')