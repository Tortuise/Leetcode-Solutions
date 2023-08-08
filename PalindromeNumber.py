class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        mid = len(x)/2
        first = x[:mid]
        second = x[mid:]
        second = second[::-1]
        if len(x) % 2 == 1:
            return x[:mid+1] == second 
   
        return first == second