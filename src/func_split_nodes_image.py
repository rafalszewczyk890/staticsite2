from func_extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        current_text = node.text
        matches = extract_markdown_images(current_text)

        if len(matches) == 0:
            new_nodes.append(node)
        else:
            for match in matches:
                concatenated_match = f"![{match[0]}]({match[1]})"
                
                split_node = current_text.split(concatenated_match, maxsplit=1)
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
                rest_matches = extract_markdown_images(split_node[1])
                if rest_matches:
                    current_text = split_node[1]
                elif len(split_node[1].strip()) > 1:
                    new_nodes.append(TextNode(split_node[1], TextType.TEXT))

    return new_nodes


'''
node = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
)
node2 = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [link](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
)
node3 = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a something.",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node, node2, node3])

print(new_nodes)
'''