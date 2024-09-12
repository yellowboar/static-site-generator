import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = ParentNode(children=[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("a", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        actual = node.to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()