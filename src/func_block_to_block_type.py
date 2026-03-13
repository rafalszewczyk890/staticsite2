import re
from htmlnode import BlockType

def block_to_block_type(block):
    if block.startswith('# ') or block.startswith('## ') or block.startswith('### ') or block.startswith('#### ') or block.startswith('##### ') or block.startswith('###### '):
        return BlockType.HEADING
    
    if block.startswith('```\n') and (block.endswith('```') or block.endswith('```\n')):
        return BlockType.CODE
    
    if block.startswith('>') or block.startswith('> '):
        block_split = block.split("\n")
        quote_flag = False
        for blockline in block_split:
            if blockline.startswith(">") or blockline.startswith("> "):
                quote_flag = True
            else:
                quote_flag = False
                break

        if quote_flag:
            return BlockType.QUOTE
        
    if block.startswith('- '):
        block_split = block.split("\n")
        uo_list_flag = False
        for blockline in block_split:
            if blockline.startswith("- "):
                uo_list_flag = True
            else:
                uo_list_flag = False
                break

        if uo_list_flag:
            return BlockType.UNORDERED_LIST
    
    if block.startswith('1. '):
        block_split = block.split("\n")
        o_list_flag = False
        for i in range(0, len(block_split)):
            if block_split[i].startswith(f"{i + 1}. "):
                o_list_flag = True
            else:
                o_list_flag = False
                break

        if o_list_flag:
            return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH