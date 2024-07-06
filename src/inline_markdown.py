import re
from textnode import TextNode, text_types


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    supported_text_types = ["text", "bold", "code", "italic"]
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_types["text"]:
            new_nodes.append(old_node)
            continue

        if old_node.text_type not in supported_text_types:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)
        # List length needs to be odd from matching delimiters
        if len(sections) % 2 == 0:
            raise ValueError(
                "Invalid Markdown: missing closing delimiter")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(
                    TextNode(sections[i], text_types["text"])
                )
            else:
                split_nodes.append(
                    TextNode(sections[i], text_type)
                )
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    # Should return [("alt name", "https://example.com/imgs/example.png"), ("another alt name", "https://example2.com/imgs/example2.png")]
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    # Should return [("link name", "https://example.com"), ("another link name", "https://example2.com")]
    pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        image_tups = extract_markdown_images(old_node.text)
        if not image_tups:
            new_nodes.append(old_node)
        else:
            current_node = TextNode(old_node.text, text_types["text"])
            for idx, image_tup in enumerate(image_tups):
                image = f"![{image_tup[0]}]({image_tup[1]})"
                sections = current_node.text.split(image, 1)
                if not sections[0] == "":
                    new_nodes.append(
                        TextNode(text=sections[0], text_type=text_types["text"]))
                new_nodes.append(
                    TextNode(text=image_tup[0], text_type=text_types["image"], url=image_tup[1]))
                if not sections[1] == "":
                    if idx != len(image_tups) - 1:
                        current_node = TextNode(
                            sections[1], text_types["text"])
                    else:
                        new_nodes.append(
                            TextNode(sections[1], text_types["text"]))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        link_tups = extract_markdown_links(old_node.text)
        if not link_tups:
            new_nodes.append(old_node)
        else:
            current_node = TextNode(old_node.text, text_types["text"])
            for idx, link_tup in enumerate(link_tups):
                link = f"[{link_tup[0]}]({link_tup[1]})"
                sections = current_node.text.split(link, 1)
                if not sections[0] == "":
                    new_nodes.append(
                        TextNode(text=sections[0], text_type=text_types["text"]))
                new_nodes.append(
                    TextNode(text=link_tup[0], text_type=text_types["link"], url=link_tup[1]))
                if not sections[1] == "":
                    if idx != len(link_tups) - 1:
                        current_node = TextNode(
                            sections[1], text_types["text"])
                    else:
                        new_nodes.append(
                            TextNode(sections[1], text_types["text"]))
    return new_nodes
