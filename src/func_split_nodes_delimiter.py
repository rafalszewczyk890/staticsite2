from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise ValueError("Incorrect formatting - closing delimiter not found")
        
        node_split = node.text.split(delimiter)
        for i in range(0, len(node_split)):
            if len(node_split[i].strip()) > 0:
                if i % 2 == 0 or i == 0:
                    new_nodes.append(TextNode(node_split[i], TextType.TEXT, None))
                else:
                    new_nodes.append(TextNode(node_split[i], text_type, None))
            else:
                continue

    return new_nodes


node = TextNode("**This** **is** a **text** with another **bold** phrase in **the** middle", TextType.TEXT, None)
node2 = TextNode("Testing this thing testing _italic_ one two", TextType.TEXT, None)
new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

for i in range (0, len(new_nodes)):
    print(i)
    print(new_nodes[i])
