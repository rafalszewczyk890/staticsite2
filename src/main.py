from func_copy_files import copy_files
from func_generate_pages_recursive import generate_pages_recursive

def main():
        copy_files("./static", "./public")
        generate_pages_recursive("./content", "./template.html", "./public")
            
main()