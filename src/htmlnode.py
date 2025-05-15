

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        prop_string = ""
        for key, value in self.props.items():
            prop_string += f" {key}=\"{value}\""
        return prop_string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        html = ""

        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return self.value
        
        html += f"<{self.tag}"
        
        if self.props:
            for prop in self.props:
                html += f" {prop}=\"{self.props[prop]}\""
        
        html += f">{self.value}</{self.tag}>"
        return html
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        html = ""
        child_html = ""

        if not self.tag:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have child nodes")
        html += f"<{self.tag}"
        if self.props:
            for prop in self.props:
                html += f" {prop}=\"{self.props[prop]}\""
        html += f">"
        for child in self.children:
            child_html += child.to_html()
        html += child_html
        html += f"</{self.tag}>"
        return html