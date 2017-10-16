""" Given a linked list, return the entry point of a cycle (if one exists). Otherwise, return None """

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

def detectCycle(head):
  """
  :type head: ListNode
  :rtype: ListNode
  """
  if head == None:
      return None
  
  slow = head
  fast = head
  meet = head
  
  while (fast.next != None and fast.next.next != None):
    slow = slow.next
    fast = fast.next.next
      
    if (slow == fast):
      while (meet != slow):
        meet = meet.next
        slow = slow.next
      return meet
  
  return None

