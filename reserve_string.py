
import unittest

class Solution(object):
    def reserve(self, string):
        try:
            for char in string:
                string.push(char)

            return string
        except Exception as e:     
            print('error' , e)      
            return "False"


class CalculatorTest(unittest.TestCase):                
    def testing(self):                   
        cal = Solution()
        self.assertEqual( cal.reserve('I am a student. How are you I am fine Thank you!') , 'you! Thank fine am I you are How student. a am I' )  

    def testing2(self):                   
        cal = Solution()
        self.assertEqual( cal.reserve('I Love Programming! What do you think?') , 'think? you do What Programming! Love I' )  

    def testing3(self):                   
        cal = Solution()
        self.assertEqual( cal.reserve('Programming') , 'Programming' )  

if __name__ == '__main__':
    unittest.main()                                      
