import unittest
from func_extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# title of the page
this is it. the title

this is another paragraph

"""
        self.assertEqual(extract_title(md), "title of the page")

    def test_no_title_multi_hash(self):
        def test_func():
            md = """
    ## title of the page
    this is it. the title

    this is another paragraph

    """
            extract_title(md)

        self.assertRaises(ValueError, test_func)

    def test_no_title_no_space(self):
        def test_func():
            md = """
    #title of the page
    this is it. the title

    this is another paragraph

    """
            extract_title(md)

        self.assertRaises(ValueError, test_func)