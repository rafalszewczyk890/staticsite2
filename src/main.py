from func_copy_files import copy_files
from func_generate_pages_recursive import generate_pages_recursive
import sys

def main():
        if len(sys.argv) > 1:
                basepath = sys.argv[1]
                print(basepath, "-basepath")
        else:
                basepath = "/"

        copy_files("./static", "./docs")
        generate_pages_recursive("./content", "./template.html", "./docs", basepath)
            
main()