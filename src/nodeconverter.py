from textnode import TextNode
from leafnode import LeafNode
from nodesplitter import *

def text_node_to_html_node(text_node : TextNode):
    match text_node.text_type:
        case TextNode.text_type_text:
            return LeafNode(None, text_node.text)
        case TextNode.text_type_bold:
            return LeafNode("b", text_node.text)
        case TextNode.text_type_italic:
            return LeafNode("i", text_node.text) 
        case TextNode.text_type_code:
            return LeafNode("code", text_node.text)
        case TextNode.text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextNode.text_type_image:
            return LeafNode("img", None, {"src" : text_node.url, "alt" : text_node.text})
        case _:
            raise Exception("Invalid text type.")
        
def text_to_textnodes(text):
    node = TextNode(text, TextNode.text_type_text)
    split_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
    split_nodes = split_nodes_delimiter(split_nodes, "*", TextNode.text_type_italic)
    split_nodes = split_nodes_delimiter(split_nodes, "`", TextNode.text_type_code)
    split_nodes = split_nodes_image(split_nodes)
    split_nodes = split_nodes_link(split_nodes)
    return split_nodes