"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
"""

import sys

class Solution(object):
    def reverse(self, x):

        if x.bit_length() > 31:
            return 0
        else:
            s2=str(abs(x))[::-1]
            reverse_num = int(s2)
            
            if(reverse_num.bit_length() > 31):
                return 0

            if (x>0):
                return reverse_num
            else:
                return -reverse_num



if __name__ == '__main__':
    result = Solution().reverse(-123)   
    print(result)