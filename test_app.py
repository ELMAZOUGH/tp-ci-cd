import unittest
from app import add
class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


    def test_add(self):
        self.assertEqual(add(2, 3), 5) [cite: 22, 23]
        self.assertEqual(add(-1, 1), 0) [cite: 24]
    
    # Nouveaux cas de tests pour améliorer la couverture
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)  # Test avec deux nombres négatifs
        
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)      # Test avec des zéros
        
    def test_add_large_numbers(self):
        self.assertEqual(add(1000, 2000), 3000) # Test avec de grands nombres
if __name__ == '__main__':
    unittest.main() [cite: 29]