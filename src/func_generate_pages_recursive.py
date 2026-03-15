from func_generate_page import generate_page
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(entry_path):
            dest_path = dest_path.replace(".md", ".html")
            print("FILE FOUND: ", entry_path, "DEST: ", dest_path)

            generate_page(entry_path, template_path, dest_path)
        else:
            generate_pages_recursive(entry_path, template_path, dest_path)


#generate_pages_recursive("../content", "../template.html", "../test_content")