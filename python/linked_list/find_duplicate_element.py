"""
Given a list of n+1 integers in the range [1, n] with exactly one element repeated (some number of times).
Find the element.
"""

"""
Think of the array as a linked list, where the value of an element is a pointer to
another element by its index in the array.

Because elements are in the range [1, n], and the array has length n+1, all of these
pointers will go to valid elements in the array.

Since some element occurs more than once, there are multiple pointers to the same 
index in the array, creating a cycle.

Use the cycle entry-point detection algorithm to find the index of this element.
"""

class Solution(object):
  def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # nums is guaranteed to have length >= 2
    slow = nums[0]
    fast = nums[nums[0]]
    meet = 0
    
    while (slow != fast):
      slow = nums[slow]
      fast = nums[nums[fast]]
    
    while(meet != slow):
      meet = nums[meet]
      slow = nums[slow]
    
    return meet