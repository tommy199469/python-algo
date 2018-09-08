
import unittest

class Solution(object):
    def find_max_profit(self, array):
        try:
            #init data 
            max_profit = 0
            first = array[0]
            for profit in array:
                if first > profit and first != profit:
                    first = profit

                if profit - first > max_profit:
                    max_profit = profit - first
            
            return max_profit
        except:
            return False


class CalculatorTest(unittest.TestCase):                
    def testing(self):                   
        cal = Solution()
        self.assertEqual(cal.find_max_profit([1, 2 ,3, 4, 5, 6]), 5)  
    def testing1(self):                   
        cal = Solution()
        self.assertEqual(cal.find_max_profit([6,5,4,3,2,1]), 0)  
    def testing2(self):                   
            cal = Solution()
            self.assertEqual(cal.find_max_profit([7,1,5,3,6,4]), 5)    
    def testing3(self):                   
                cal = Solution()
                self.assertEqual(cal.find_max_profit([5,4,2,5,7,1,3]), 5) 
    def testing4(self):                   
                cal = Solution()
                self.assertEqual(cal.find_max_profit([4,9,1,3]), 5)   
    def testing5(self):                   
                cal = Solution()
                self.assertEqual(cal.find_max_profit([3,7,2,6,3]), 4) 
    def testing6(self):                   
                cal = Solution()
                self.assertEqual(cal.find_max_profit([5,4,3,2,7]), 5) 
    def testing7(self):                   
                cal = Solution()
                self.assertEqual(cal.find_max_profit([1,1,1,1]), 0)
    def testing8(self):                   
                cal = Solution()
                self.assertEqual(cal.find_max_profit([33,45,34,63,80,23,75]), 52)
if __name__ == '__main__':
    unittest.main()                                      
