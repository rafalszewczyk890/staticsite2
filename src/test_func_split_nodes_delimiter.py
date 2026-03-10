from func_split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestSplitNodes(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is a text with _an italic_ phrase in the middle", TextType.TEXT, None)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(3, len(new_nodes))
        self.assertEqual(new_nodes[1], TextNode("an italic", TextType.ITALIC))

    def test_raise_missing_close(self):
        def raise_error():
            node = TextNode("This is a text with _an italic phrase in the middle", TextType.TEXT, None)
            split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertRaises(ValueError, raise_error)

    def test_multiple_delmiters(self):
        node = TextNode("This is a text with **a bold** phrase in **the** middle", TextType.TEXT, None)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(5, len(new_nodes))
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)

    def test_multiple_nodes(self):
        node = TextNode("This is a text with **a bold** phrase in **the** middle", TextType.TEXT, None)
        node2 = TextNode("**This** is a **text** with another **bold** phrase in **the** middle", TextType.TEXT, None)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)

        self.assertEqual(13,len(new_nodes))

    def test_consecutive_delimiter(self):
        node = TextNode("This is a text with **a bold** phrase in **the** middle", TextType.TEXT, None)
        node2 = TextNode("**This** **is** a **text** with another **bold** phrase in **the** middle", TextType.TEXT, None)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)

        self.assertEqual(14,len(new_nodes))