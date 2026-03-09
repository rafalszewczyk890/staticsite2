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
    

html_node = HTMLNode("testTag", "testValue", None, {"testProp1": "value1", "testProp2": "value2"})

print(html_node)
print(html_node.props_to_html())