import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # HTML node tests

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

    # leaf node tests

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

    # parent node tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_nested(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("parent", [
                    LeafNode("li", "list"),
                    LeafNode("a", "link text"),
                    ParentNode("parent", [
                    LeafNode("li", "list22"),
                    LeafNode("a", "link text22"),
                    
                ], 
                {"class": "nestedParent22"})
                ], 
                {"class": "nestedParent"})
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<parent><li>list</li><a>link text</a><parent><li>list22</li><a>link text22</a></parent></parent></p>")

    def test_no_tag(self):
        def nodeWithoutTag():
            node = ParentNode(tag=None, children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")], props=None) # type: ignore
            
        self.assertRaises(ValueError, nodeWithoutTag)


    def test_no_children(self):
        def nodeWithoutTag():
            node = ParentNode(tag=None, children=[], props=None) # type: ignore
            
        self.assertRaises(ValueError, nodeWithoutTag)