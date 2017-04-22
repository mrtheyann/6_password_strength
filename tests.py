import unittest

from password_strength import get_password_strength as gps


class QuadraticEquationTestCase(unittest.TestCase):
    def test_blacklisted(self):
        '''Test if password in blacklist'''
        self.assertEqual(gps('111111'), 1)
        self.assertEqual(gps('qwerty123'), 1)
        self.assertEqual(gps('98765432'), 1)

    def test_lowercase(self):
        '''Test if password is lowercase'''
        self.assertEqual(gps('lowercase'), 3)
        self.assertEqual(gps('foobarbaz'), 3)

    def test_uppercase(self):
        '''Test if password is uppercase'''
        self.assertEqual(gps('UPPERCASE'), 3)
        self.assertEqual(gps('FOOBARBAZ'), 3)
    
    def test_date(self):
        '''Test if there is a date in password'''
        self.assertEqual(gps('dude1998'), 4)
        self.assertEqual(gps('01011977'), 3)
    
    def test_num(self):
        '''Test if password is number-only'''
        self.assertEqual(gps('1337322'), 3)
        self.assertEqual(gps('17291729'), 3)
    
    def test_medium(self):
        '''Test medium strength passwords'''
        self.assertEqual(gps('IAmTheKing'), 4)
        self.assertEqual(gps('W@porize'), 5)
    
    def test_strong(self):
        '''Test strong passwords'''
        self.assertEqual(gps('T1m31992'), 7)
        self.assertEqual(gps('Ub3rP@sswrd'), 10)
        self.assertEqual(gps('Cl@rify1'), 10)


if __name__ == '__main__':
    unittest.main()
