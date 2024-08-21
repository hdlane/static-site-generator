def extract_title(markdown):
    # 1. Pull the h1 header from the markdown file and return it
    # 2. If none, return Exception
    # 3. extract_title("# Hello") should return "Hello"
    pass


def generate_page(from_path, template_path, dest_path):
    # 1. Print a message like "Generating page from from_path to dest_path using template_path".
    # 2. Read the markdown file at from_path and store the contents in a variable.
    # 3. Read the template file at template_path and store the contents in a variable.
    # 4. Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    # 5. Use the extract_title function to grab the title of the page.
    # 6. Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    # 7. Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    pass
