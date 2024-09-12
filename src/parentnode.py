from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent nodes must have tags.")
        
        if not self.children:
            raise ValueError("Parent nodes must have children.")
        
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        
        return f"<{self.tag}>{html_string}</{self.tag}>"

