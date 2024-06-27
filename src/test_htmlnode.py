import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_parent_node_leaf_only(self):
        children = [
            LeafNode("b", "Bold Text"),
            LeafNode(None, "Normal Text"),
            LeafNode("i", "Italic Text"),
            LeafNode("a", "Link Text", {
                     "href": "https://example.com", "target": "_blank"}),
        ]
        node = ParentNode("p", children, None)
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal Text<i>Italic Text</i><a href=\"https://example.com\" target=\"_blank\">Link Text</a></p>"
        )

    def test_nested_parent_node(self):
        parent_children = [
            LeafNode("b", "Bold Text"),
            LeafNode("i", "Italic Text"),
        ]
        children = [
            LeafNode("b", "Bold Text"),
            LeafNode(None, "Normal Text"),
            ParentNode("div", parent_children),
            LeafNode("i", "Italic Text"),
            LeafNode("a", "Link Text", {
                     "href": "https://example.com", "target": "_blank"}),
        ]
        node = ParentNode("p", children, None)
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal Text<div><b>Bold Text</b><i>Italic Text</i></div><i>Italic Text</i><a href=\"https://example.com\" target=\"_blank\">Link Text</a></p>"
        )


if __name__ == "__main__":
    unittest.main()
