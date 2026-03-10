from htmlnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError("Text type must be a value within TextType Enum")
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, None)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, None)
    
    if text_node.text_type == TextType.LINK:
        if text_node.url is None or len(text_node.url) == 0:
            raise ValueError("URL must be provided for LINK nodes")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        if text_node.url is None or len(text_node.url) == 0:
            raise ValueError("URL must be provided for LINK nodes")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
