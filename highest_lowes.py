
import unittest

class Solution(object):
    def HighAndLow(self, string):
        try:
            #init data
            if not string:
                return ""
            
            str_array = list(map(str, string.split())) 
            # print(str_array)
            min_number = str_array[0]
            max_number = str_array[0]
            for char in str_array:
                if char.lstrip('-+').isnumeric():
                    min_number 

                    if char < min_number:
                        min_number = char
                   
                    if char > max_number:
                        max_number = char
                                

            return (max_number if max_number.lstrip('-+').isnumeric() else "") if max_number == min_number else str(max_number) +" " +str(min_number)
        except Exception as e:     
            print(e)      
            return "False"


class CalculatorTest(unittest.TestCase):                
    def testing(self):                   
        cal = Solution()
        self.assertEqual( cal.HighAndLow("1 2 3 4 5") , "5 1")  

    def testing2(self):                   
        cal = Solution()
        self.assertEqual( cal.HighAndLow("1 9 3 4 -5") , "9 -5")  

    def testing3(self):                   
        cal = Solution()
        self.assertEqual( cal.HighAndLow("7 % A 1 3") , "7 1")  

    def testing4(self):                   
        cal = Solution()
        self.assertEqual( cal.HighAndLow("1 1 1 1") , "1")  

    def testing5(self):                   
        cal = Solution()
        self.assertEqual( cal.HighAndLow("") , "")  
        
    def testing6(self):                   
        cal = Solution()
        self.assertEqual( cal.HighAndLow("A B C D E") , "")  

if __name__ == '__main__':
    unittest.main()                                      
