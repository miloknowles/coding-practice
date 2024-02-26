from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
  value: float | int | None
  left: Optional['Node'] = None
  right: Optional['Node'] = None


def insert(root: Node, value: float | int):
  """Insert `value` into the binary search tree rooted at `root`."""
  if root.value is None:
    root.value = value
  else:
    # Should go in the right subtree
    if value >= root.value:
      if root.right is None:
        root.right = Node(value=value, left=None, right=None)
      else:
        insert(root.right, value)

    # Should go in the left subtree
    else:
      if root.left is None:
        root.left = Node(value=value, left=None, right=None)
      else:
        insert(root.left, value)


def build_tree(values: list[int | float]) -> Node:
  """Builds a tree with values and returns the root node."""
  root = Node(value=None, left=None, right=None)
  for v in values:
    insert(root, v)
  return root


def inorder_traversal_stack(root: Node) -> list[int | float]:
  values = []

  stack = []
  current_node = root

  while len(stack) > 0 or current_node is not None:
    if current_node is not None:
      stack.append(current_node)
      current_node = current_node.left

    # If we can't go left any further, add the parent value (top of the stack)
    # and then go to the right subtree.
    else:
      parent = stack.pop()
      values.append(parent.value)
      current_node = parent.right

  return values


def inorder_traversal_recursive(root: Node) -> list[int | float]:
  if root is None:
    return []
  return (
    inorder_traversal_recursive(root.left) + \
    [root.value] + \
    inorder_traversal_recursive(root.right)
  )


root = build_tree([i for i in range(100)])
# print(inorder_traversal_stack(root))
print(inorder_traversal_recursive(root))