from htmlnode import HTMLNode, LeafNode, ParentNode

block_types = {
    "paragraph": "paragraph",
    "heading": "heading",
    "code": "code",
    "quote": "quote",
    "unordered_list": "unordered_list",
    "ordered_list": "ordered_list",
}


def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split('\n\n')
    for section in sections:
        if section == "":
            continue
        section = section.strip()
        blocks.append(section)
    return blocks


def block_to_block_type(markdown):
    lines = markdown.split("\n")
    # Headings
    if (
        markdown.startswith("# ")
        or markdown.startswith("## ")
        or markdown.startswith("### ")
        or markdown.startswith("#### ")
        or markdown.startswith("##### ")
        or markdown.startswith("###### ")
    ):
        return block_types["heading"]
    # Code
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_types["code"]
    # Quote
    if markdown.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_types["paragraph"]
        return block_types["quote"]
    # Unordered List
    if markdown.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_types["paragraph"]
        return block_types["unordered_list"]
    if markdown.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_types["paragraph"]
        return block_types["unordered_list"]
    # Ordered List
    if markdown.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_types["paragraph"]
            i += 1
        return block_types["ordered_list"]
    return block_types["paragraph"]


def paragraph_to_html_node(block):
    return LeafNode(tag="p", value=block)


def heading_to_html_node(block):
    if block.startswith("# "):
        return LeafNode(tag="h1", value=block.strip("# "))
    if block.startswith("## "):
        return LeafNode(tag="h2", value=block.strip("## "))
    if block.startswith("### "):
        return LeafNode(tag="h3", value=block.strip("### "))
    if block.startswith("#### "):
        return LeafNode(tag="h4", value=block.strip("#### "))
    if block.startswith("##### "):
        return LeafNode(tag="h5", value=block.strip("##### "))
    if block.startswith("###### "):
        return LeafNode(tag="h6", value=block.strip("###### "))


def code_to_html_node(block):
    stripped_block = block.strip("```")
    return ParentNode(tag="pre", children=[LeafNode("code", stripped_block)])


def quote_to_html_node(block):
    stripped_block = []
    lines = block.split("> ")

    for line in lines:
        if not line == "":
            stripped_block.append(line)

    stripped_block = " ".join(stripped_block)
    return LeafNode(tag="blockquote", value=stripped_block)


def ol_to_html_node(block):
    child_nodes = []
    lines = block.split("\n")
    i = 1
    for line in lines:
        text = line.strip(f"{i}. ")
        child_nodes.append(LeafNode("li", text))
        i += 1
    return ParentNode(tag="ol", children=child_nodes)


def ul_to_html_node(block):
    child_nodes = []
    lines = block.split("\n")
    if lines[0].startswith("- "):
        for line in lines:
            text = line.strip("- ")
            child_nodes.append(LeafNode("li", text))
    if lines[0].startswith("* "):
        for line in lines:
            text = line.strip("* ")
            child_nodes.append(LeafNode("li", text))
    return ParentNode(tag="ul", children=child_nodes)


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
