import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child_node = HTMLNode("p", None, None, None)

        node = HTMLNode("p", "testValue", [child_node], {"testTag": "testVal"})
        node2 = HTMLNode("p", "testValue", [child_node], {"testTag": "testVal"})

        self.assertEqual(node, node2)

    def test_eq_empty(self):
        node = HTMLNode(None, None, None, None)
        node2 = HTMLNode(None, None, None, None)

        self.assertEqual(node, node2)

    def test_not_eq(self):
        child_node = HTMLNode("p", None, None, None)

        node = HTMLNode("p", "testValue", [child_node], {"testTag": "testVal"})
        node2 = HTMLNode("p", "testValue", [child_node, child_node], {"testTag": "testVal"})

        self.assertNotEqual(node, node2)

    def test_string_repr(self):

        node = HTMLNode("p", "testValue", ["test_child"], {"testTag": "testVal"})
        self.assertEqual(node.props_to_html(), "testTag=\"testVal\"")

    def test_eq_leaf(self):

        node = LeafNode("a", "link value", {"url": "http://test.com"})
        node2 = LeafNode("a", "link value", {"url": "http://test.com"})

        self.assertEqual(node, node2)

    def test_neq_leaf(self):

        node = LeafNode("a", "link value")
        node2 = LeafNode("a", "link value", {"url": "http://test.com"})

        self.assertNotEqual(node, node2)

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html2(self):
        node = LeafNode("p", "Hello, world!", {"class": "helloWorld", "url": "http://net.dot"})
        
        self.assertEqual(node.to_html(), "<p class=\"helloWorld\" url=\"http://net.dot\">Hello, world!</p>")

    def test_leaf_to_html3(self):
        node = LeafNode(None, "Hello, world!")
        
        self.assertEqual(node.to_html(), "Hello, world!")