from func_split_nodes_delimiter import split_nodes_delimiter
from func_split_nodes_image import split_nodes_image
from func_split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = TextNode(text, TextType.TEXT)
    split_bold = split_nodes_delimiter([nodes], "**", TextType.BOLD)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
    split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE)
    split_link = split_nodes_link(split_code)
    split_image = split_nodes_image(split_link)

    return split_image
