import unittest
from models import new
New = new.New

class NewTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the New class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_new = New()

    def test_instance(self):
        self.assertTrue(is instance(self.new_new, New))


if __name__ == '__main__':
    unittest.main()