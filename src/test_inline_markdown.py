import unittest
from textnode import (
    TextNode,
    text_types
)
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("Text with a **bold** word", text_types["text"])
        new_nodes = split_nodes_delimiter([node], "**", text_types["bold"])
        self.assertListEqual(
            [
                TextNode("Text with a ", text_types["text"]),
                TextNode("bold", text_types["bold"]),
                TextNode(" word", text_types["text"])
            ],
            new_nodes
        )

    def test_delim_italic(self):
        node = TextNode("Text with a *italic* word", text_types["text"])
        new_nodes = split_nodes_delimiter([node], "*", text_types["italic"])
        self.assertListEqual(
            [
                TextNode("Text with a ", text_types["text"]),
                TextNode("italic", text_types["italic"]),
                TextNode(" word", text_types["text"])
            ],
            new_nodes
        )

    def test_delim_code(self):
        node = TextNode("Text with a `code` word", text_types["text"])
        new_nodes = split_nodes_delimiter([node], "`", text_types["code"])
        self.assertListEqual(
            [
                TextNode("Text with a ", text_types["text"]),
                TextNode("code", text_types["code"]),
                TextNode(" word", text_types["text"])
            ],
            new_nodes
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "Text with a **bold** word and **another**", text_types["text"])
        new_nodes = split_nodes_delimiter([node], "**", text_types["bold"])
        self.assertListEqual(
            [
                TextNode("Text with a ", text_types["text"]),
                TextNode("bold", text_types["bold"]),
                TextNode(" word and ", text_types["text"]),
                TextNode("another", text_types["bold"]),
            ],
            new_nodes
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "Text with a **bold word** and **another**", text_types["text"])
        new_nodes = split_nodes_delimiter([node], "**", text_types["bold"])
        self.assertListEqual(
            [
                TextNode("Text with a ", text_types["text"]),
                TextNode("bold word", text_types["bold"]),
                TextNode(" and ", text_types["text"]),
                TextNode("another", text_types["bold"]),
            ],
            new_nodes
        )

    def test_delim_multitype(self):
        node = TextNode("Text with **bold** and *italic*", text_types["text"])
        new_nodes = split_nodes_delimiter([node], "**", text_types["bold"])
        self.assertListEqual(
            [
                TextNode("Text with ", text_types["text"]),
                TextNode("bold", text_types["bold"]),
                TextNode(" and *italic*", text_types["text"]),
            ],
            new_nodes
        )
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_types["italic"])
        self.assertListEqual(
            [
                TextNode("Text with ", text_types["text"]),
                TextNode("bold", text_types["bold"]),
                TextNode(" and ", text_types["text"]),
                TextNode("italic", text_types["italic"]),
            ],
            new_nodes
        )

    def test_delim_incomplete_bold(self):
        node = TextNode("Text with **incomplete bold", text_types["text"])
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", text_types["bold"])

    def test_extract_markdown_images(self):
        text = "Extract this ![alt text](https://example.com/imgs/example.png) image"
        images_tuple = extract_markdown_images(text)
        self.assertListEqual(
            [("alt text", "https://example.com/imgs/example.png")],
            images_tuple
        )

    def test_extract_markdown_no_images(self):
        text = "Do not extract this (https://example.com/imgs/example.png) image"
        images_tuple = extract_markdown_images(text)
        self.assertListEqual(
            [],
            images_tuple
        )

    def test_extract_markdown_image_with_link(self):
        text = "Extract this ![alt text](https://example.com/imgs/example.png) image, but not this [link name](https://example.com) link"
        images_tuple = extract_markdown_images(text)
        self.assertListEqual(
            [("alt text", "https://example.com/imgs/example.png")],
            images_tuple
        )

    def test_extract_markdown_multiple_images(self):
        text = "Extract this ![alt text](https://example.com/imgs/example.png) image, and another ![another alt text](https://example.com/imgs/example2.png) image"
        images_tuple = extract_markdown_images(text)
        self.assertListEqual(
            [("alt text", "https://example.com/imgs/example.png"),
             ("another alt text", "https://example.com/imgs/example2.png")],
            images_tuple
        )

    def test_extract_markdown_links(self):
        text = "Extract this [link name](https://example.com) link"
        links_tuple = extract_markdown_links(text)
        self.assertListEqual(
            [("link name", "https://example.com")],
            links_tuple
        )

    def test_extract_markdown_no_links(self):
        text = "Do not extract this (https://example.com/imgs/example.png) link"
        links_tuple = extract_markdown_links(text)
        self.assertListEqual(
            [],
            links_tuple
        )

    def test_extract_markdown_link_with_image(self):
        text = "Extract this [link name](https://example.com) link, but not this ![alt text](https://example.com/imgs/example.png) image"
        links_tuple = extract_markdown_links(text)
        self.assertListEqual(
            [("link name", "https://example.com")],
            links_tuple
        )

    def test_extract_markdown_multiple_links(self):
        text = "Extract this [link name](https://example.com) link, and another [another link name](https://example2.com) link"
        links_tuple = extract_markdown_links(text)
        self.assertListEqual(
            [("link name", "https://example.com"),
             ("another link name", "https://example2.com")],
            links_tuple
        )


if __name__ == "__main__":
    unittest.main()
