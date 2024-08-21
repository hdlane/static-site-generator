import os


from htmlnode import LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_types = {
    "paragraph": "paragraph",
    "heading": "heading",
    "code": "code",
    "quote": "quote",
    "unordered_list": "unordered_list",
    "ordered_list": "ordered_list",
}


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_types["heading"]
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_types["code"]
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_types["paragraph"]
        return block_types["quote"]
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_types["paragraph"]
        return block_types["unordered_list"]
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_types["paragraph"]
        return block_types["unordered_list"]
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_types["paragraph"]
            i += 1
        return block_types["ordered_list"]
    return block_types["paragraph"]


def markdown_to_html_node(markdown):
    # Convert a whole markdown document into an HTMLNode
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_types["heading"]:
            html_nodes.append(heading_to_html_node(block))
            continue
        if block_type == block_types["paragraph"]:
            html_nodes.append(paragraph_to_html_node(block))
            continue
        if block_type == block_types["code"]:
            html_nodes.append(code_to_html_node(block))
            continue
        if block_type == block_types["quote"]:
            html_nodes.append(quote_to_html_node(block))
            continue
        if block_type == block_types["unordered_list"]:
            html_nodes.append(ul_to_html_node(block))
            continue
        if block_type == block_types["ordered_list"]:
            html_nodes.append(ol_to_html_node(block))
    return ParentNode(tag="div", children=html_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ul_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def extract_title(markdown):
    first_line = markdown.split('\n\n')[0]
    if first_line.startswith("# "):
        return first_line.strip("# ")
    else:
        return Exception("No h1 header at top of file")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    markdown = ""
    html = ""

    with open(from_path, 'r') as f:
        markdown += f.read()

    with open(template_path, 'r') as f:
        html += f.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(html)
