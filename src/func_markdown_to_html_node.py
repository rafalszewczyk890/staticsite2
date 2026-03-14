from htmlnode import BlockType, HTMLNode, LeafNode, ParentNode
from func_markdown_to_blocks import markdown_to_blocks
from func_block_to_block_type import block_to_block_type
from func_text_nd_to_html_nd import text_node_to_html_node
from func_text_to_textnodes import text_to_textnodes

def text_to_children(text):
    children = []
    split_text = text_to_textnodes(text)
    for child in split_text:
        children.append(text_node_to_html_node(child))

    return children

def markdown_to_html_node(markdown):
    child_nodes = []

    markdown_split = markdown_to_blocks(markdown)
    for block in markdown_split:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            fragment_to_check = block[0:7]
            hash_count = fragment_to_check.count("#")
            stripped_text = block.lstrip("#").strip()
            children = text_to_children(stripped_text)
            new_node = ParentNode(f"h{hash_count}", children)
            child_nodes.append(new_node)

        if block_type == BlockType.CODE:
            stripped_text = block.strip("```").lstrip()
            new_node = ParentNode("pre", [LeafNode("code", stripped_text)])
            child_nodes.append(new_node)

        if block_type == BlockType.QUOTE:
            lines = block.split("\n")
            lines_list = []
            for line in lines:
                stripped_line = line.lstrip(">").strip()
                lines_list.append(stripped_line)

            joined_block = " ".join(lines_list)
            children = text_to_children(joined_block)
            new_node = ParentNode("blockquote", children)
            child_nodes.append(new_node)

        if block_type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            joined_block = " ".join(lines)
            children = text_to_children(joined_block)
            new_node = ParentNode("p", children)
            child_nodes.append(new_node)

        if block_type == BlockType.UNORDERED_LIST:
            node_list = []
            split_block = block.split("\n")
            for block in split_block:
                block = block.lstrip("-").strip()
                node_list.append(ParentNode("li", text_to_children(block)))
            new_node = ParentNode("ul", node_list)
            child_nodes.append(new_node)

        if block_type == BlockType.ORDERED_LIST:
            node_list = []
            split_block = block.split("\n")
            for block in split_block:
                block_wo_dot = block.split(".")
                block = block_wo_dot[1].strip()
                node_list.append(ParentNode("li", text_to_children(block)))
            new_node = ParentNode("ol", node_list)
            child_nodes.append(new_node)

    parent_div = ParentNode("div", child_nodes)
    return parent_div


'''
markdown = """### Text Text **blablal bold** and the _italic_ hehe

text2 line

line another

```
This is a code block```

> this are quotes
> this is quote too

- unordered list
- lalal
- bjbjb
- qti

1. ordered **bold** list
2. this is one
3. third option
4. fourth
"""

markdown2 = "This is a paragraph lblablla _italic_ although also **bold**"

print(markdown_to_html_node(markdown).to_html())
#print(text_to_children(markdown2))

'''