import unittest

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divsion(a,b):
    return a / b

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        sum= add(10, 5)
        self.assertEqual(sum, 15)
    
    def test_add2(self):
        sum= add(-5.000000000000000000000001, 5)
        self.assertEqual(sum, -.000000000000000000000001)

    
class testCaseSub(unittest.TestCase):
    def test_sub(self):
       sub= subtract(10, 5)
       self.assertEqual(sub, 5) 
    def test_sub2(self):
       sub= subtract(10, "5")
       self.assertEqual(sub, 5)

class testCaseMult(unittest.TestCase):
    def test_mult(self):
        mult = multiply(10, 2)
        self.assertEqual(mult, 20)
    def test_mult2(self):
        mult= multiply(10.10, 5)
        self.assertEqual(mult, 50.50)
    def test_mult3(self):
        mult= multiply(-50000000000000, 3.2)
        self.assertEqual(mult, -160000000000000)
    
class testCaseDiv(unittest.TestCase):
    def test_div(self):
        div = divsion(5.0, 4)
        self.assertEqual(div, 1.25)
    def test_div2(self):
        div = divsion(10, 11)
        self.assertEqual(div, .9091)
   
if __name__ == '__main__':
    unittest.main()
    


