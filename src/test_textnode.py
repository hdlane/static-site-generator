import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text,
                        "https://example.com")
        node2 = TextNode("This is a text node", text_type_text,
                         "https://example.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", text_type_text,
                        "https://example.com")
        node2 = TextNode("This is a text node", text_type_text, url=None)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a different text node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test node", text_type_text,
                        "https://example.com")
        self.assertEqual(
            "TextNode(This is a test node, text, https://example.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
