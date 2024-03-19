from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def reverse_iterative(head: ListNode):
  """Returns the head of the reversed list."""
  # 0 -> 1 -> 2 -> 3
  current = head
  prev = None
  while current.next is not None:
    next = current.next
    current.next = prev
    prev = current
    current = next
  current.next = prev
  return current


def reverse(head: ListNode) -> tuple[ListNode, ListNode]:
  """Returns the head and tail of the reversed list."""
  # Base case: a singleton list doesn't need to be reversed.
  if head.next is None:
    return head, head

  # Remove the head and reverse the remaining list.
  sublist_head, sublist_tail = reverse(head.next)

  # Add the head to the end of the list.
  sublist_tail.next = head
  
  # The head should have no next item.
  head.next = None

  return sublist_head, head


class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
      return None
    # return reverse(head)[0]
    return reverse_iterative(head)