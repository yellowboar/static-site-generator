from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have values.")
        
        if not self.tag:
            return self.value
        
        html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        return html_string