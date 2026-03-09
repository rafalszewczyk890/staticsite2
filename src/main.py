from textnode import TextType, TextNode

def main():
    node = TextNode("This is a test", TextType.CODE, "testlink.url")
    print(node)

main()