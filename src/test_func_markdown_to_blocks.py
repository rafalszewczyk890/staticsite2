from func_markdown_to_blocks import markdown_to_blocks
import unittest

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = '''This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items'''
        

        
        self.assertListEqual(markdown_to_blocks(text), ["This is **bolded** paragraph", "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line","- This is a list\n- with items"])

    def test_one_block(self):
        text = "This is **bolded** paragraph"

        self.assertListEqual(markdown_to_blocks(text), ["This is **bolded** paragraph"])

    def test_no_block(self):
        text = ""

        self.assertListEqual(markdown_to_blocks(text), [])

    def test_excessive_newline(self):
        text = '''This is **bolded** paragraph

        
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items'''
        

        
        self.assertListEqual(markdown_to_blocks(text), ["This is **bolded** paragraph", "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line","- This is a list\n- with items"])