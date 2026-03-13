import unittest
from func_block_to_block_type import block_to_block_type
from htmlnode import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        text = "### heading text"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_heading_no_white(self):
        text = "###heading text"
        self.assertNotEqual(block_to_block_type(text), BlockType.HEADING)

    def test_code(self):
        text = """```
        code text
        ```"""
        self.assertEqual(block_to_block_type(text), BlockType.CODE)

    def test_code_no_newline(self):
        text = """```code text```"""
        self.assertNotEqual(block_to_block_type(text), BlockType.CODE)

    def test_quote(self):
        text = """> quote text
> hhh"""
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_uo(self):
        text = """- unordered
- list"""
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_uo_false(self):
        text = """- unordered
< list"""
        self.assertNotEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_ordered(self):
        text = """1. ordered
2. list
3. text
4. text2"""
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)

    def test_ordered_unordered(self):
        text = """1. ordered
67. list
3. text
4. text2"""
        self.assertNotEqual(block_to_block_type(text), BlockType.ORDERED_LIST)