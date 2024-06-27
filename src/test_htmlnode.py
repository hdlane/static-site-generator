import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://example.com", "target": "_blank"}
        node = HTMLNode("<a>", "Example.com", None, props)
        self.assertEqual(
            node.props_to_html(),
            " href=\"https://example.com\" target=\"_blank\""
        )

    def test_repr(self):
        node = HTMLNode("h1", "Test Heading1")
        self.assertEqual(
            "HTMLNode(h1, Test Heading1, None, None)", repr(node)
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            node.to_html(),
            "<p>Hello, world!</p>"
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(
            node.to_html(),
            "Hello, world!"
        )


if __name__ == "__main__":
    unittest.main()
