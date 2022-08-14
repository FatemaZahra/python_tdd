# python_tdd

## Test-Driven-Development

When writing good quality code we need to make sure our functions are fully tested. The process we will use to achieve this is called test-driven-development.

![image](https://user-images.githubusercontent.com/102330725/183909708-1e6b7af4-af3d-4616-97d4-da8b5181cfa6.png)


First we need to decide on what behaviour we would like to test. We will start with the simplest behaviour first. Once that is working we can add another piece of functionality and test that independently. This allows us to build up to an eventual solution so that we don't have to solve the whole problem at once.

### Red - green - refactor cycle
This process is referred to as the red-green-refactor cycle

- We first decide what functionality we want to implement.
- Write a test for it, watch it fail (red)
- Write the minimum amount of code that will make that test pass (green)
- Refactor code if necessary
- Repeat.

#### Benefits

- Helps to develop the logic in our code
- Research studies demonstrate that TDD is a technique that has the most impact in the quality of the code developers write.
- Code has fewer bugs
- Easy to add functionality to your code
- Code can be understood easily

### Example code 
#### Test
```python
from calc import SimpleCalc
import unittest
import pytest

class Caltests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(2, 2), 1)

    def test_percentage(self):
        self.assertEqual(self.calc_obj.percentage(2, 2), 100)

    def test_convert_cm_to_m(self):
        self.assertEqual(self.calc_obj.convert_cm_to_m(1), 0.01)

    def test_dob(self):
        self.assertEqual(self.calc_obj.dob(1), 2021)
```
#### Code
```python
class SimpleCalc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1/value2

    def percentage(self, value1, value2):
        return (value1/value2)*100
    
    def convert_cm_to_m(self, value1):
        return value1 * 0.01

    def dob(self, age):
        year = 2022 - age
        return year
```
