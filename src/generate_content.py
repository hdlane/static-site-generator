import os

from block_markdown import markdown_to_html_node


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for file in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(content_path):
            if (dest_path.endswith(".md")):
                dest_path = dest_path.replace(".md", ".html")
            print(f"Generating page from {content_path} to {
                  dest_path} using {template_path}")

            markdown = ""
            html = ""

            with open(content_path, 'r') as f:
                markdown += f.read()

            with open(template_path, 'r') as f:
                html += f.read()

            title = extract_title(markdown)
            content = markdown_to_html_node(markdown).to_html()

            html = html.replace("{{ Title }}", title)
            html = html.replace("{{ Content }}", content)

            # os.makedirs(os.path.dirname(dest_dir_path), exist_ok=True)

            with open(dest_path, 'w') as f:
                f.write(html)
        else:
            generate_page_recursive(content_path, template_path, dest_path)


def extract_title(markdown):
    first_line = markdown.split('\n\n')[0]
    if first_line.startswith("# "):
        return first_line.strip("# ")
    else:
        return Exception("No h1 header at top of file")
