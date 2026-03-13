from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1,
    HEADING = 2,
    CODE = 3,
    QUOTE = 4,
    UNORDERED_LIST = 5,
    ORDERED_LIST = 6

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        if self.props is None:
            return props_string
        
        else:
            for prop in self.props:
                props_string += f"{prop}=\"{self.props[prop]}\" "

            return props_string.strip()
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        
        return False
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.children = None

    def to_html(self):
        html_string = ""
        
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            html_string = self.value
            return html_string
        
        if self.props is not None and len(self.props) > 0:
            props_string = self.props_to_html()
            html_string = f"<{self.tag} {props_string}>{self.value}</{self.tag}>"
            return html_string

        else:
            html_string = f"<{self.tag}>{self.value}</{self.tag}>"
            return html_string
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Tag argument is required")
        
        if children is None or len(children) == 0:
            raise ValueError("Children argument is required")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):        
        html_children = ""
        if self.children is not None:
            for child in self.children:
                html_children += child.to_html()
        
        html_node = f"<{self.tag}>{html_children}</{self.tag}>"

        return html_node