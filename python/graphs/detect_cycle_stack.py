def detect_cycles(g: dict[str, list[str]]):
  """Detect cycles in a directed graph."""
  completed = set()
  stack = []
  current_node = list(g.keys())[0]
  ancestors = set([current_node])

  while len(stack) > 0 or current_node is not None:
    # Time to backtrack
    if current_node is None:
      current_node = stack.pop()
      completed.add(current_node)
      ancestors.remove(current_node)

    # Otherwise, recurse on children
    else:
      for child in g[current_node]:
        if child in ancestors:
          return True
        ancestors.add(child)
        stack.append(child)

  return False


graph_with_cycles = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : ['9'],
  '9': []
}

graph_without_cycles = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : ['9'],
  '9': []
}


detect_cycles(graph_with_cycles)