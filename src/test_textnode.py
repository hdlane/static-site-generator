import unittest

from textnode import (
    TextNode,
    text_types,
    text_node_to_html_node,
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
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        node2 = TextNode("Bold Text", text_types["bold"])
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "b")
        node3 = TextNode("Italic Text", text_types["italic"])
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "i")
        node4 = TextNode("Code Text", text_types["code"])
        html_node4 = text_node_to_html_node(node4)
        self.assertEqual(html_node4.tag, "code")
        node5 = TextNode(
            "Link Text", text_types["link"], "https://example.com")
        html_node5 = text_node_to_html_node(node5)
        self.assertEqual(html_node5.tag, "a")
        node6 = TextNode(
            "Image Text", text_types["image"], "https://example.com")
        html_node6 = text_node_to_html_node(node6)
        self.assertEqual(html_node6.tag, "img")
        with self.assertRaises(ValueError):
            node7 = TextNode("Invalid text_type", "class")
            html_node7 = text_node_to_html_node(node7)


if __name__ == "__main__":
    unittest.main()
