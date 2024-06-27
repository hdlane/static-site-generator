import unittest

from textnode import (
    TextNode,
    text_types
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_types["text"])
        node2 = TextNode("This is a text node", text_types["text"])
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_types["text"],
                        "https://example.com")
        node2 = TextNode("This is a text node", text_types["text"],
                         "https://example.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", text_types["text"],
                        "https://example.com")
        node2 = TextNode("This is a text node", text_types["text"], url=None)
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", text_types["text"])
        node2 = TextNode("This is a text node", text_types["bold"])
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", text_types["text"])
        node2 = TextNode("This is a different text node", text_types["text"])
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test node", text_types["text"],
                        "https://example.com")
        self.assertEqual(
            "TextNode(This is a test node, text, https://example.com)", repr(node)
        )

    def test_text_node_to_html_node(self):
        node = TextNode("Raw Text", text_types["text"])
        self.assertEqual(
            repr(node.text_node_to_html_node()),
            "LeafNode(None, Raw Text, None)"
        )
        node2 = TextNode("Bold Text", text_types["bold"])
        self.assertEqual(
            repr(node2.text_node_to_html_node()),
            "LeafNode(b, Bold Text, None)"
        )
        node3 = TextNode("Italic Text", text_types["italic"])
        self.assertEqual(
            repr(node3.text_node_to_html_node()),
            "LeafNode(i, Italic Text, None)"
        )
        node4 = TextNode("Code Text", text_types["code"])
        self.assertEqual(
            repr(node4.text_node_to_html_node()),
            "LeafNode(code, Code Text, None)"
        )
        node5 = TextNode(
            "Link Text", text_types["link"], "https://example.com")
        self.assertEqual(
            repr(node5.text_node_to_html_node()),
            "LeafNode(a, Link Text, {'href': 'https://example.com'})"
        )
        node6 = TextNode(
            "Image Text", text_types["image"], "https://example.com")
        self.assertEqual(
            repr(node6.text_node_to_html_node()),
            "LeafNode(img, , {'src': 'https://example.com', 'alt': 'Image Text'})"
        )
        node7 = TextNode("Invalid text_type", "class")
        self.assertRaises(Exception)


if __name__ == "__main__":
    unittest.main()
