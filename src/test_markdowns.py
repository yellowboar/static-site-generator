import unittest
from markdownfunctions import *

class TestMarkdowns(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = (
            """# This is a heading

            This is a paragraph of text. It has some **bold** and *italic* words inside of it.

            * This is the first list item in a list block
            * This is a list item
            * This is another list item"""
        )
        expected = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n" 
            + "* This is a list item\n"
            + "* This is another list item"    
        ]
        actual = markdown_to_blocks(markdown)
        self.assertEqual(expected, actual)

    def test_block_to_blocktype_heading(self):
        block = "###### This is a heading\n"
        self.assertEqual("heading", block_to_block_type(block))
        
        block2 = "####### This is a heading\n"
        self.assertEqual("Not valid heading syntax.", block_to_block_type(block2))
        
        block3 = "#######This is a heading\n"
        self.assertEqual("Not valid heading syntax.", block_to_block_type(block3))

    def test_block_to_blocktype_code(self):
        block = "```This is a code block```\n"
        self.assertEqual("code", block_to_block_type(block))
        
        block2 = "``This is a code block``\n"
        self.assertEqual("Not valid code syntax.", block_to_block_type(block2))

    def test_block_to_blocktype_code(self):
        block = ">This is a quote block\n"
        self.assertEqual("quote", block_to_block_type(block))
        
        block2 = "> This is a quote block\n"
        self.assertEqual("quote", block_to_block_type(block2))

    def test_block_to_blocktype_unordered_list(self):
        block = "* This is an unordered list\n"
        self.assertEqual("unordered list", block_to_block_type(block))
        
        block2 = "- This is also an unordered list\n"
        self.assertEqual("unordered list", block_to_block_type(block2))
    
    def test_block_to_blocktype_ordered_list(self):
        block = "1. This is an ordered list\n"
        self.assertEqual("ordered list", block_to_block_type(block))
    
    # test markdown to html

    def test_md_to_html_heading(self):
        md = (
            """### This is a *heading*
            # This is a sub heading"""
        )
        expected = [HTMLNode("h3", children=[HTMLNode(None, "This is a "), HTMLNode("i", "heading")]), 
                    HTMLNode("h1", children=[HTMLNode(None, "This is a sub heading")])]
        actual = markdown_to_html_node(md)
        self.assertEqual(expected, actual)
    
    def test_md_to_html_paragraph(self):
        md = (
            """This is a paragraph of text. It has some **bold** and *italic* words inside of it.
            This is still part of the paragraph."""
        )
        expected = [HTMLNode("p", children=[HTMLNode(None, "This is a paragraph of text. It has some "), 
                                            HTMLNode("b", "bold"), 
                                            HTMLNode(None, " and "), 
                                            HTMLNode("i", "italic"), 
                                            HTMLNode(None, " words inside of it."),
                                            HTMLNode(None, "This is still part of the paragraph.")])]
        actual = markdown_to_html_node(md)
        self.assertEqual(expected, actual)
    
    def test_md_to_html_quote(self):
        md = (
            """>This is a quote of text. It has some **bold** and *italic* words inside of it.
            >This is still part of the quote."""
        )
        expected = [HTMLNode("blockquote", children=[HTMLNode(None, "This is a quote of text. It has some "), 
                                    HTMLNode("b", "bold"), 
                                    HTMLNode(None, " and "), 
                                    HTMLNode("i", "italic"), 
                                    HTMLNode(None, " words inside of it."),
                                    HTMLNode(None, "This is still part of the quote.")])]
        actual = markdown_to_html_node(md)
        self.assertEqual(expected, actual)

    def test_md_to_html_code(self):
        md = (
            """```This is a quote of text formatted as code. It has some **bold** and *italic* words inside of it.
            This is still part of the quote.```"""
        )
        expected = [HTMLNode("pre", children=[HTMLNode("code", children=[HTMLNode(None, "This is a quote of text formatted as code. It has some "), 
                                    HTMLNode("b", "bold"), 
                                    HTMLNode(None, " and "), 
                                    HTMLNode("i", "italic"), 
                                    HTMLNode(None, " words inside of it."),
                                    HTMLNode(None, "This is still part of the quote.")])])]
        actual = markdown_to_html_node(md)
        self.assertEqual(expected, actual)
        
    # def test_markdown_to_html_node(self):
    #     markdown = (
    #         """
    #         ## This is a *heading*
    #         # This is a sub heading

    #         This is a paragraph of text. It has some **bold** and *italic* words inside of it.
    #         This is still part of the paragraph.

    #         * This is the **first list** item in a list block
    #         * This is a list item
    #         * This is another list item
            
    #         1. This is the `first item` in an ordered list
    #         2. This is the second.
    #         """
    #     )
    #     lst = markdown_to_html_node(markdown)
    #     print(lst)
        