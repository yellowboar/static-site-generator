import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }

        node = HTMLNode(props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_empty_props(self):
        node = HTMLNode()
        actual = node.props_to_html()
        self.assertEqual("", actual)

    def test_init_all_none(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

if __name__ == "__main__":
    unittest.main()
