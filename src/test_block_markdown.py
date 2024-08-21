import unittest
from block_markdown import (
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node
)
from generate_content import extract_title


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocks
        )

    def test_markdown_to_blocks_newlines(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line




* This is a list
* with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocks
        )

    def test_markdown_block_to_blocktype(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "unordered_list")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "ordered_list")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_markdown_to_html_node(self):
        markdown = """Hello, world!

* One
* Two

1. One
2. Two

```
code
```

# Heading 1

> Quote one
> Quote two"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Hello, world!</p><ul><li>One</li><li>Two</li></ul><ol><li>One</li><li>Two</li></ol><pre><code>code\n</code></pre><h1>Heading 1</h1><blockquote>Quote one Quote two</blockquote></div>"
        )

    def test_extract_title(self):
        markdown1 = """# Heading1

Paragraph"""
        title1 = extract_title(markdown1)
        self.assertEqual(
            title1,
            "Heading1"
        )
        markdown2 = """Paragraph

# Heading1"""
        title2 = extract_title(markdown2)
        self.failureException(
            title2
        )


if __name__ == "__main__":
    unittest.main()
