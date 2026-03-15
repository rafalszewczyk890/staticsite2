def extract_title(markdown):
    split_markdown = markdown.split("\n")
    for line in split_markdown:
        if line[0:2] == "# ":
            return line.strip("# ").strip()
        
    raise ValueError("No page title found")