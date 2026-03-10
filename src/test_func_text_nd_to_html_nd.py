from func_text_nd_to_html_nd import text_node_to_html_node
from htmlnode import LeafNode
from textnode import TextType, TextNode
import unittest

class TestTextNodeToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        if html_node is not None:
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD, "test.url")
        html_node = text_node_to_html_node(node)
        if html_node is not None:
            self.assertEqual(html_node.props, None)
            self.assertEqual(html_node.tag, "b")

    def test_link(self):
        node = TextNode("Link text", TextType.LINK, "test.url")
        html_node = text_node_to_html_node(node)
        if html_node is not None and html_node.props is not None:
            self.assertEqual(html_node.props["href"], "test.url")
        
    def test_img(self):
        node = TextNode("Alt text", TextType.IMAGE, "test.url")
        html_node = text_node_to_html_node(node)
        if html_node is not None and html_node.props is not None:
            self.assertEqual(html_node.props["src"], "test.url")
            self.assertEqual(html_node.props["alt"], "Alt text")

    def test_raise_error_image(self):
        
        def convert_node():
            node = TextNode("Alt text", TextType.IMAGE, None)
            return text_node_to_html_node(node)
        
        self.assertRaises(ValueError, convert_node)