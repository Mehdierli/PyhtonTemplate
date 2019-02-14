# -*- coding: utf-8 -*-

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>0:
            n = n/3
            if n == 1:
                return True
        return False

sl = Solution()
print(sl.isPowerOfThree(9))