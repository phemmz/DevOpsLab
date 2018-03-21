import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from src import app

class MyTest(unittest.TestCase):
  def test_my_function(self):
    self.assertEqual(app.my_function(1, 1), 2)
    self.assertEqual(app.my_function(1, -1), 0)
    self.assertEqual(app.my_function(1, 0), 1)
    self.assertEqual(app.my_function(-1, -1), -2)
    self.assertEqual(app.my_function(1.0, 1), 2)
    self.assertEqual(app.my_function(1.1, 1.1), 2.2)

if __name__ == '__main__':
  unittest.main()
