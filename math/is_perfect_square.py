""" Determine whether a positive integer 'num' is a perfect square without using built in sqrt. """

# Using binary search: O(log n)
def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 16:
        return (num in [0, 1, 4, 9, 16])
    else:
        minX = 0
        maxX = int(num / 4) + 1 # all perfect squares above 16 have a root less than n/4

        while(maxX - minX > 1):
            guess = int(minX + (maxX - minX) / 2)
            if guess ** 2 == num:
                return True
            elif guess ** 2 < num:
                minX = guess
            else:
                maxX = guess
        return False

# Using one simple odd number trick: O(sqrt(n))
def isPerfectSquare2(num):
    """
    A square number is always 1 + 3 + 5 + 7 + .... + more odd numbers... 
    """
    sub = 1
    while (num > 0):
        num -= sub
        sub += 2
    return num == 0