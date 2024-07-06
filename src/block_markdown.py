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
