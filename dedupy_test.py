#!/usr/bin/python3
import unittest, os
from unittest.case import expectedFailure
from dedupy import hash_files

class HashFilesTest(unittest.TestCase):
    def test_hash_cwd(self):
        testcase = os.getcwd()
        filename = os.path.join(os.getcwd(), 'LICENSE')
        filehash = '1ebbd3e34237af26da5dc08a4e440464'
        self.assertEqual(hash_files(testcase)[filename], filehash)
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