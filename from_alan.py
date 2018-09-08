"""
buildEquations([-1, 2, -3, 4, -5, 6, -11, 12, -13], 32)
print(buildEquations([2, 1, 4, 3, 6, 7, 8, 10], 42), end="\n\n")
"""

import sys

class Solution(object):
    def reverse(self, x , y):
        target = y
        max_value = x[-1] + x [-2]
        xyz = []
        final_result = []
        for item in x:
            result = target/item
            if(result <= max_value and result % 1 == 0 and item !=1):
                xyz.append(item) 
                xyz.append(int(result)) 
                break

        if(xyz):
            for i in xyz:
                if i in x and i not in final_result:
                    final_result.append(i)
                else:
                    for y in x:
                        if(y>1 and y not in final_result ):
                            cal = i-y
                            if cal not in final_result and y not in final_result:
                                final_result.append(str(cal)+'+'+str(y) )
                                break

        return final_result if final_result else "Max reange is " +str(max_value*x[-1])


if __name__ == '__main__':
    result = Solution().reverse([1,2,3,4,5,6,7,8,9,10] ,200)   
    print(result)