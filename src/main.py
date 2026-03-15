from func_copy_files import copy_files
from func_generate_page import generate_page

def main():
        copy_files("./static", "./public")
        generate_page("./content/index.md", "./template.html", "./public/index.html")
    
main()