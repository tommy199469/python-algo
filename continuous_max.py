
import unittest

class Solution(object):
    def findContinuousNumbers(self, numbers , start=0 , end = 1, biggest_sum = 0.0 , biggest_result = []):
        try:
            current_result = []
            current_sum = 1.0
            for index, item in enumerate(numbers[start:]):
                current_result.append(item)
                current_sum = current_sum *item
                if index == len(numbers) -end:
                    break

            if current_sum > biggest_sum:
                biggest_result = current_result
                biggest_sum = float(current_sum)
            
            if start == len(numbers):
                return biggest_result
            else:
                if end == len(numbers):
                    start += 1
                    end = start
                else:
                    end +=1

                return Solution.findContinuousNumbers(self,numbers , start , end ,biggest_sum , biggest_result)

            return []
        except Exception as e:     
            print('error' , e)      
            return "False"


class CalculatorTest(unittest.TestCase):                
    def testing(self):                   
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-2.5, 4, 0, 3, 0.5, 8, -1] ) , [3, 0.5, 8] )  

    def testing2(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-1,-2,-1,-4,0] ) , [-1,-2,-1,-4] )  

    def testing3(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-1,-2,-3,0,1,1] ) , [-2,-3] )  

    def testing4(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-1,2,0,3,-1] ) , [3] )  

    def testing5(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-2.5,4,0,3,0.5,8,1,1,3,0,10,11,12,1,-1,2,3,4,5,-10] ) , [10,11,12,1,-1,2,3,4,5,-10] )  

    def testing6(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-2.5,4,0,3,0.5,8,0,1,3,0,10,11,12,1,-1,2,3] ) , [10,11,12,1] )  

    def testing7(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [2,1] ) , [2,1] )  

    def testing8(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-2.5,4,0,3,0.5,8,0,1,3,0,-1,10,11,12,1,2,3] ) , [10,11,12,1,2,3] )  

    def testing9(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-2.5,4,0,3,0.5,8,0,1,3,0,-1,10,11,12,1,2,3] ) , [10,11,12,1,2,3] )  

    def testing10(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [10,1,3,-2,4,3,2,1] ) , [10,1,3] )  

    def testing11(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [-1.3,-2,-3,1.9] ) , [-2,-3,1.9] )  

    def testing12(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [5,0] ) , [5] )  


    def testing13(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [0,1] ) , [1] )  
        
    def testing14(self):                      
        cal = Solution()
        self.assertEqual( cal.findContinuousNumbers( [2,1,2,3,0,-10,5,6,7,-2,8,-1] ) , [-10,5,6,7,-2,8] )  

if __name__ == '__main__':
    unittest.main()                                      
