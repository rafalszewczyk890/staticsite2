def markdown_to_blocks(markdown):
    block_list = markdown.split("\n\n")
    new_list = list(filter(lambda b: len(b) > 0, map(lambda block: block.strip(), block_list)))
    return new_list

