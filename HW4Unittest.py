#HW #4 Unit Testing
import unittest

# Question 1 
def cube_volume(s):
    return s**3

class testCasecube(unittest.TestCase): #unit test for volume of a cube
    def test_cube(self): 
       cube= cube_volume(2)
       self.assertEqual(cube, 8) 
    def test_cube2(self): 
       cube= cube_volume(-1)
       self.assertEqual(cube, 1)
    def test_cube3(self): 
       cube= cube_volume(1/2)
       self.assertEqual(cube, .125)
     
#Question 2
def list_avg(list):
    length = len(list)
    return (sum(list) / length )

class testCaseAvg(unittest.TestCase): #unit test for average of list elements
    def test_avg(self): 
       avg= list_avg([1,2,3,4,5])
       self.assertEqual(avg, 3) 
    def test_avg2(self):
        avg = list_avg([])
        self.assertEqual(avg, 0 )
    def test_avg3(self):
        avg = list_avg([-5,0,-4,1,1.5,4.1/5,])
        self.assertEqual(avg, -0.95)


#question 3
def first_last(f, l):
    return f + l


class testCasename(unittest.TestCase): #unit test for first and last name function
    def test_name(self): 
        name = first_last("Bhaveesh", " Beemireddy")
        self.assertEqual(name, "Bhaveesh Beemireddy")
    def test_name1(self): 
       name= first_last("Sai Bhaveesh", "beemireddy")
       self.assertEqual(name, "Sai Bhaveesh beemireddy") 
    def test_name2(self):
        name = first_last("Bhaveesh", "Beemireddy")
        self.assertEqual(name, "Bhaveesh Beemireddy")


    


if __name__ == '__main__':
    unittest.main()




