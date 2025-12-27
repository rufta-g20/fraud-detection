import unittest
from src.processing import ip_to_int

class TestPreprocessing(unittest.TestCase):
    def test_ip_conversion(self):
        self.assertEqual(ip_to_int("192.168.1.1"), 3232235777)
        self.assertEqual(ip_to_int("invalid-ip"), 0) # Tests the error handling

if __name__ == '__main__':
    unittest.main()