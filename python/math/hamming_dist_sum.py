""" Given a list of integers, find the sum of all pairwise hamming distances. """
import math

# Long solution, doesn't run in time
class Solution(object):
  def int2bin(self, n, size=32):
    binary = ''
    power_vals = range(0, size)
    power_vals.reverse()
    
    for power in power_vals:
      exp = 2 ** power
      if (exp <= n) and n != 0:
        binary += '1'
        n -= exp
      else:
         binary += '0'
    return binary

  def hamming_dist(self, a, b):
    """ Assumed a and b have the same length. """
    d = 0
    for i in range(len(a)):
      d += int(a[i]) ^ int(b[i])
    return d
  
  def totalHammingDistance(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
      return 0
    
    size = int(math.log(max(nums))) + 1
    total = 0
    bins = [self.int2bin(n) for n in nums]
    
    for ii in range(len(nums)-1):
      for jj in range(ii+1, len(nums)):
        total += self.hamming_dist(bins[ii], bins[jj])
    return total

# Example: '{0:032b}'.format(3) converts 3 to 32 bit binary string padded with leading zeros
# map(fn, list) applies fn to every item in the list
# zip(arg1, arg2) takes in any number of iterables and returns a list of tuples with the corresponding els from each
# zip(*listoftuples) unzips a zipped list back into it's components

# formats each number into binary
# unzipping the list of bitstrings creates 32 tuples, one for each bit in the string
# each tuple has one entry for each of the numbers
# multiple num zeros times num ones because every zero has distance one from every one

def totalHammingDistance(nums):
  binaries = map('{:032b}'.format, nums)
  bit_tuples = zip(*binaries)
  return sum(b.count('0') * b.count('1') for b in bit_tuples)


if __name__ == '__main__':
  nums = [4, 14, 2]
  ans = 6

  res = totalHammingDistance(nums)
  print("Result: %d Answer: %d" % (res, ans))
  # assert(res == ans, "Error: did not get expected output. %d is not %d" % (res, ans))