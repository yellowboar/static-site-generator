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

if __name__ == "__main__":
    unittest.main()