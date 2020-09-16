import unittest

def intSort(x):
    x.sort()
    return x

class testSorting(unittest.TestCase):
    
    def test_intSort(self):
        x = [3, 4, 2, 1]
        self.assertTrue(intSort(x) == [1, 2, 3, 4])
        
if __name__ == '__main__':
    unittest.main()