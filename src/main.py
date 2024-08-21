import os
import shutil


def main():
    copy_contents("static", "public")


# Recursive function that copies all contents from a
# source directory to a destination directory
# For example, "static" to "public"
# 1. Deletes all contents in the destination
# 2. Copy all files and subdirectories, nested files, etc.
# 3. Log the path of each file copied for debugging

# Figure out how to get pathing down correctly "../static/"
def copy_contents(src, dst):
    if not os.path.exists(src):
        raise Exception("Source does not exist")
    if dst == "public" and os.path.exists("public"):
        print("Cleaning 'public' folder")
        shutil.rmtree("public")
        os.mkdir("public")
    elif not os.path.exists("public"):
        print("public folder does not exist! Creating...")
        os.mkdir("public")

    src_files = os.listdir(src)
    for file in src_files:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        if os.path.isdir(src_path):
            os.mkdir(dst_path)
            print(f"Creating directory {dst_path}")
            copy_contents(src_path, dst_path)
        else:
            print(f"Copying {src_path} to {dst_path}")
            shutil.copy(src_path, dst_path)


main()
