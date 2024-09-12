import unittest

from textnode import TextNode
from leafnode import LeafNode
from nodeconverter import text_node_to_html_node
from nodesplitter import split_nodes_delimiter

class TestNodeFunctions(unittest.TestCase):
    def test_case_text(self):
        node = TextNode("This is a text node.", "text", "https://bum.com")
        leaf_node = text_node_to_html_node(node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertIsNone(leaf_node.tag)
        self.assertEqual("This is a text node.", leaf_node.value)

    def test_case_bold(self):
        node = TextNode("This is a text node.", "bold", "https://bum.com")
        leaf_node = text_node_to_html_node(node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual("b", leaf_node.tag)
        self.assertEqual("This is a text node.", leaf_node.value)

    def test_case_italic(self):
        node = TextNode("This is a text node.", "italic", "https://bum.com")
        leaf_node = text_node_to_html_node(node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual("i", leaf_node.tag)
        self.assertEqual("This is a text node.", leaf_node.value)

    def test_case_code(self):
        node = TextNode("This is a text node.", "code", "https://bum.com")
        leaf_node = text_node_to_html_node(node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual("code", leaf_node.tag)
        self.assertEqual("This is a text node.", leaf_node.value)

    def test_case_link(self):
        node = TextNode("This is a text node.", "link", "https://bum.com")
        leaf_node = text_node_to_html_node(node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual("a", leaf_node.tag)
        self.assertEqual("This is a text node.", leaf_node.value)
        self.assertEqual({"href": "https://bum.com"}, leaf_node.props)

    def test_case_image(self):
        node = TextNode("This is a text node.", "image", "https://bum.com")
        leaf_node = text_node_to_html_node(node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual("img", leaf_node.tag)
        self.assertIsNone(leaf_node.value)
        self.assertEqual({"src": "https://bum.com", "alt": "This is a text node."}, leaf_node.props)

    # testing node splitter

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        expected = [
            TextNode("This is text with a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_code),
            TextNode(" word", TextNode.text_type_text),
        ]
        actual = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_mult_markdowns(self):
        node = TextNode("This is *text* with a *code block* word", TextNode.text_type_text)
        expected = [
            TextNode("This is ", TextNode.text_type_text),
            TextNode("text", TextNode.text_type_bold),
            TextNode(" with a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_bold),
            TextNode(" word", TextNode.text_type_text),
        ]
        actual = split_nodes_delimiter([node], "*", TextNode.text_type_bold)
        self.assertEqual(expected, actual)
    
    def test_split_nodes_mult_nodes(self):
        node = TextNode("This is *text* with a *code block* word", TextNode.text_type_text)
        node2 = TextNode("Other text *here*", TextNode.text_type_text)
        expected = [
            TextNode("This is ", TextNode.text_type_text),
            TextNode("text", TextNode.text_type_bold),
            TextNode(" with a ", TextNode.text_type_text),
            TextNode("code block", TextNode.text_type_bold),
            TextNode(" word", TextNode.text_type_text),
            TextNode("Other text ", TextNode.text_type_text),
            TextNode("here", TextNode.text_type_bold)
        ]
        actual = split_nodes_delimiter([node, node2], "*", TextNode.text_type_bold)
        self.assertEqual(expected, actual)        
        
if __name__ == "__main__":
    unittest.main()