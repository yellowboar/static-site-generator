import unittest

from textnode import TextNode
from leafnode import LeafNode
from nodeconverter import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node_1 = TextNode("This is a text node.", "bold")
        node_2 = TextNode("This is a text node.", "bold")
        self.assertEqual(node_1, node_2)
    
    def test_not_eq(self):
        node_1 = TextNode("This is a text node.", "bold")
        node_2 = TextNode("This is not a text node.", "italic")
        self.assertNotEqual(node_1, node_2)

    def test_with_url(self):
        node_1 = TextNode("This is a text node.", "bold", "https://bum.com")
        node_2 = TextNode("This is a text node.", "bold", "https://bum.com")
        self.assertEqual(node_1, node_2)

    # testing text node to leaf node converter

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

if __name__ == "__main__":
    unittest.main()