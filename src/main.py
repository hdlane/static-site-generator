import os
import shutil

from copystatic import copy_files_recursive
from generate_content import generate_page_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_template = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public files...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_page_recursive(
        dir_path_content, dir_path_template, dir_path_public)


main()
