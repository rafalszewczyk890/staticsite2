import unittest
from func_text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(text)

        self.assertListEqual(textnodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_text_with_italics_only(self):
        text = "This is _italic_ test of _italic_ words _test_"
        textnodes = text_to_textnodes(text)

        self.assertListEqual(textnodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" test of ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" words ", TextType.TEXT),
            TextNode("test", TextType.ITALIC),
        ])

    def test_text_no_markup(self):
        text = "This is normal text without markup markers."
        textnodes = text_to_textnodes(text)

        self.assertListEqual(textnodes, [
            TextNode("This is normal text without markup markers.",TextType.TEXT),
        ])