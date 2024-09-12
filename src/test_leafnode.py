import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_values(self):
        node = LeafNode(None, tag="p")
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html_no_tag(self):
        node = LeafNode(value="This is a leaf node.")
        expected = "This is a leaf node."
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_to_html(self):
        node = LeafNode("Click me!", "a", props={"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        actual = node.to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()