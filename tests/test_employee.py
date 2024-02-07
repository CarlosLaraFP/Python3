# python3 -m unittest discover -s tests

import unittest
from hello.employee import Employee

class TestSomeFunction(unittest.TestCase):
    
    def test_from_name_and_years(self):
        emp = Employee.from_name_and_years("Jane Smith", 5)
        self.assertEqual(emp.years_of_service(), 5)
        #self.assertNotEqual(some_function(2, 2), 5)

if __name__ == '__main__':
    unittest.main()
