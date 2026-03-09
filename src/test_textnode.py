import unittest

from textnode import TextNode, TextType

class TextTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_eq_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.TEXT, "url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "url.com")

        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT, "url.com")
        node2 = TextNode("This is a text node 2", TextType.TEXT, "url.com")

        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "url.com")
        node2 = TextNode("This is a text node", TextType.TEXT, "url2.com")

        self.assertNotEqual(node, node2)

    def test_wrong_text_type(self):
        def create_node():
            node = TextNode("This is a text node", TextType.TEST, "url.com") # type: ignore


        self.assertRaises(AttributeError, create_node)

if __name__ == "__main__":
    unittest.main