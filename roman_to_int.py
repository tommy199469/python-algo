"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

import sys
import re

import timeit
class Solution(object):
    def romanToInt(self, s):
        roman = ['I' , 'V' , 'X' , 'L', 'C' , "D" , "M"]
        value = [1,5,10,50,100,500,1000]
        str_list = [y for y in re.split('([I|V|X|L|C|D|M])',str(s)) if y is not '']
        result = 0
        old_str = value[roman.index(str_list[0])]
        for val in str_list:
            result += int(value[roman.index(val)])
            if value[roman.index(val)] > old_str:
                result -= old_str*2

            old_str = value[roman.index(val)]
        return result




if __name__ == '__main__':
    start = timeit.default_timer()
    result = Solution().romanToInt("IV")   
    print(result)
    stop = timeit.default_timer()
    print ((stop - start)*100 )