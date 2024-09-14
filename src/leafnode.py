from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        
        if not self.value:
            raise ValueError("Leaf nodes must have values.")
        
        if not self.tag:
            return self.value
        
        html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        return html_string

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"