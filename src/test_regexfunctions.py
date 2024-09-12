import unittest
from imglinkextractor import extract_markdown_images
from imglinkextractor import extract_markdown_links

class TestRegexFunctions(unittest.TestCase):
    def test_extract_images(self):
        text = ("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)" 
            + " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
                    ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

    def test_extract_images_empty(self):
        text = "This is plain text"
        expected = []
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
    
    def test_extract_links(self):
        text = ("This is text with a link [to boot dev](https://www.boot.dev)"
            + " and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected = [("to boot dev", "https://www.boot.dev"), 
                    ("to youtube", "https://www.youtube.com/@bootdotdev")]
        actual = extract_markdown_links(text)

    def test_extract_links_empty(self):
        text = "This is plain text"
        expected = []
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)