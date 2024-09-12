import unittest

from textnode import TextNode
from leafnode import LeafNode
from nodeconverter import text_node_to_html_node
from nodesplitter import *

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
        
    def test_split_img(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
                        + " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", 
                        TextNode.text_type_text)
        node2 = TextNode("Other text with a ![cat](https://cat.com/cat.png)", 
                         TextNode.text_type_text)
        
        expected = [
            TextNode("This is text with a ", TextNode.text_type_text),
            TextNode("rick roll", TextNode.text_type_image, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextNode.text_type_text),
            TextNode("obi wan", TextNode.text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode("Other text with a ", TextNode.text_type_text),
            TextNode("cat", TextNode.text_type_image, "https://cat.com/cat.png")
        ]
        actual = split_nodes_image([node, node2])
        self.assertEqual(expected, actual)

    def test_split_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)"
                        + " and [to youtube](https://www.youtube.com/@bootdotdev)", 
                        TextNode.text_type_text)
        node2 = TextNode("Other text with a link [to cat](https://cat.com)", 
                         TextNode.text_type_text)
        expected = [
            TextNode("This is text with a link ", TextNode.text_type_text),
            TextNode("to boot dev", TextNode.text_type_link, "https://www.boot.dev"),
            TextNode(" and ", TextNode.text_type_text),
            TextNode("to youtube", TextNode.text_type_link, "https://www.youtube.com/@bootdotdev"),
            TextNode("Other text with a link ", TextNode.text_type_text),
            TextNode("to cat", TextNode.text_type_link, "https://cat.com")
        ]
        actual = split_nodes_link([node, node2])
        self.assertEqual(expected, actual)
    
    def test_split_img_no_img(self):
        node = TextNode("This is text.", 
                        TextNode.text_type_text)
        node2 = TextNode("Other text.", 
                         TextNode.text_type_text)
        self.assertEqual([node, node2], split_nodes_image([node, node2]))

    def test_split_link_no_link(self):
        node = TextNode("This is text.", 
                        TextNode.text_type_text)
        node2 = TextNode("Other text.", 
                         TextNode.text_type_text)
        self.assertEqual([node, node2], split_nodes_image([node, node2]))

    def test_split_img_no_text(self):
        node = TextNode(None, TextNode.text_type_text)
        node2 = TextNode("Other text with a ![cat](https://cat.com/cat.png)", 
                         TextNode.text_type_text)
        expected = [
            TextNode("Other text with a ", TextNode.text_type_text),
            TextNode("cat", TextNode.text_type_image, "https://cat.com/cat.png")
        ]
        actual = split_nodes_image([node, node2])
        self.assertEqual(expected, actual)

    def test_split_img_no_text(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)"
                        + " and [to youtube](https://www.youtube.com/@bootdotdev)", 
                        TextNode.text_type_text)
        node2 = TextNode(None, TextNode.text_type_text)
        expected = [
            TextNode("This is text with a link ", TextNode.text_type_text),
            TextNode("to boot dev", TextNode.text_type_link, "https://www.boot.dev"),
            TextNode(" and ", TextNode.text_type_text),
            TextNode("to youtube", TextNode.text_type_link, "https://www.youtube.com/@bootdotdev"),
        ]
        actual = split_nodes_link([node, node2])
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()