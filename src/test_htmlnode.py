import unittest

from htmlnode import HTMLNode

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