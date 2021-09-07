#!/usr/bin/python3
import unittest
from dedupy import hash_files

class HashFilesTest(unittest.TestCase):
    def test_no_path(self):
        testcase = None
        expected = "No path given"
        self.assertEqual(hash_files(testcase), expected)
    def test_invalid_path1(self):
        testcase = "1234"
        expected = "Invalid path"
        self.assertEqual(hash_files(testcase), expected)
    def test_invalid_path2(self):
        testcase = "I'm a test string"
        expected = "Invalid path"
        self.assertEqual(hash_files(testcase), expected)

if __name__ == '__main__':
    unittest.main()