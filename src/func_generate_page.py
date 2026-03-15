from func_markdown_to_html_node import markdown_to_html_node
from func_extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath=None):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        markdown = file.read()

    with open(template_path) as template_file:
        template = template_file.read()

    html_string = markdown_to_html_node(markdown).to_html()  
    title = extract_title(markdown)

    template_replaced = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace("href=\"/", f"href=\"/{basepath}").replace("src=\"/", f"src=\"/{basepath}")

    dir = os.path.dirname(dest_path)
    filename = os.path.basename(dest_path)
    print(dir)
    print(filename)

    if not os.path.exists(dir):
        os.makedirs(dir)
        f = open(dest_path, "x")
        f.write(template_replaced)
        f.close()

    else:
        f = open(dest_path, "w")
        f.write(template_replaced)
        f.close()

    


#generate_page("../content/index.md", "../template.html", "../public/blabla/test/gg/index.html")