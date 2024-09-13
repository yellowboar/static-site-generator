import re
from htmlnode import HTMLNode
from nodeconverter import *
from nodesplitter import *

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    for i, line in enumerate(lines):
        lines[i] = line.strip()
        
    block = []
    for line in lines:
        if line == "":
            if len(block) == 0:
                continue
            if len(block) == 1:
                blocks.append(block[0])
            else:
                blocks.append("\n".join(block))
            block = []
            continue
        block.append(line)

    if len(block) == 1:
        blocks.append(block[0])
    else:
        blocks.append("\n".join(block)) 
    return blocks

def block_to_block_type(block):
    match block[0]:
        case "#":
            if re.match(r"^#{1,6} .+", block):
                return "heading"
            else:
                return "Not valid heading syntax."
        case "`":
            if re.match(r"^\`{3}", block):
                return "code"
            else:
                return "Not valid code syntax." 
        case ">":
            if re.match(r"^>", block):
                return "quote"
            else:
                return "Not valid quote syntax."       
        case "*" | "-":
            if re.match(r"^(\*|-) .+", block):
                return "unordered list"
            else:
                return "Not valid unordered list syntax."
        case _:
            if re.match(r"^(\d+\.) .+", block):
                return "ordered list"
            else:
                return "normal"       
        
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        match block_to_block_type(block):
            case "heading":
                nodes.extend(heading_block_to_html_node(block))
            case "unordered list":
                nodes.append(ul_block_to_html_node(block))
            case "ordered list":
                nodes.append(ol_block_to_html_node(block))
            case "code":
                nodes.append(code_block_to_html_node(block))
            case "quote":
                nodes.append(quote_block_to_html_node(block))
            case "normal":
                nodes.append(paragraph_block_to_html_node(block))              
    return HTMLNode("div", children=nodes)

def heading_block_to_html_node(block):
    lines = block.splitlines()
    heading_nodes = []
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        first_space = line.index(" ")
        num_hashes = line[:first_space].count("#")
        text = line[first_space + 1:]
        children = text_to_children(text)
        heading_nodes.append(HTMLNode("h" + str(num_hashes), children=children))
    return heading_nodes

def ul_block_to_html_node(block):
    lines = block.splitlines()
    list_nodes = []
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        first_space = line.index(" ")
        text = line[first_space + 1:]
        children = text_to_children(text)
        list_nodes.append(HTMLNode("li", children=children))
    return HTMLNode("ul", children=list_nodes)

def ol_block_to_html_node(block):
    lines = block.splitlines()
    list_nodes = []
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        first_space = line.index(" ")
        text = line[first_space + 1:]
        children = text_to_children(text)
        list_nodes.append(HTMLNode("li", children=children))
    return HTMLNode("ol", children=list_nodes)

def code_block_to_html_node(block):
    lines = block.splitlines()
    code_nodes = []
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        if line.startswith("```"):
            line = line[3:]
        if line.endswith("```"):
            line = line[:-3]
        children = text_to_children(line)
        code_nodes.extend(children)
    return HTMLNode("pre", children=[HTMLNode("code", children=code_nodes)])

def paragraph_block_to_html_node(block):
    lines = block.splitlines()
    paragraph_nodes = []
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        children = text_to_children(line)
        paragraph_nodes.extend(children)
    return HTMLNode("p", children=paragraph_nodes)

def quote_block_to_html_node(block):
    lines = block.splitlines()
    quote_nodes = []
    for line in lines:
        if line.endswith("\n"):
            line = line[:-1]
        children = text_to_children(line[1:])
        quote_nodes.extend(children)
    return HTMLNode("blockquote", children=quote_nodes)

def text_to_children(text):
    nodes = text_to_textnodes(text)
    leaf_nodes = []
    for node in nodes:
        leaf_nodes.append(text_node_to_html_node(node))
    return leaf_nodes

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        line.strip()
        if line.startswith("# "):
            return line[2:]
    
    raise Exception("No title found.")