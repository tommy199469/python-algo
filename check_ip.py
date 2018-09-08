
"""
    IP Validation by range [ 0.0.0.0 - 255.255.255.255 ]
"""

import unittest

class Solution(object):
    def is_valid_IP(self, ip):
        try:
            if not ip:
                return False

            max_ip_slot = 255
            min_ip_slot = 0
            ip_array = ip.split('.')

            if len(ip_array) != 4:
                return False

            for slot in ip_array:
                if not slot.isnumeric() or (slot[0] == '0' and len(slot) != 1):
                    return False

                if min_ip_slot > int(slot) or int(slot) > max_ip_slot:
                    return False
            return True
        except Exception as e:     
            print(e)      
            return False

class CalculatorTest(unittest.TestCase):                
    def testing(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('12.255.56.1'), True)  

    def testing2(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP(''), False)  

    def testing3(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('abc.def.ghi.jkl'), False)  

    def testing4(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('123.456.789.0'), False)  

    def testing5(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('112.34.56'), False)  

    def testing6(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('12.34.56 .1'), False)  

    def testing7(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('123.045.067.089'), False)  

    def testing8(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('127.1.1.0'), True)  

    def testing9(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('0.0.0.0'), True)  

    def testing10(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('.0.0.0'), False)  


    def testing11(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('0.34.82.53'), True)  


    def testing12(self):                   
        cal = Solution()
        self.assertEqual(cal.is_valid_IP('192.168.1.300'), False)  

if __name__ == '__main__':
    unittest.main()                                      
