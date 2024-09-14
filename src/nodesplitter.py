from textnode import TextNode
from imglinkextractor import extract_markdown_images
from imglinkextractor import extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_list = []
    split_nodes = []
    punctuation = ":.,()"
    for node in old_nodes:
        if node.text_type != TextNode.text_type_text:
            split_nodes.append(node)
            continue
        if len(node.text.split(delimiter)) == 1:
            split_nodes.append(node)
            continue
        split_list.extend(node.text.split(delimiter))
        for seq in split_list:
            if not seq:
                continue
            if seq.endswith("\n"):
                seq = seq[:-1]

            if (seq[0] != " " and (seq[0] not in punctuation) and 
                seq[-1] !=  " " and (seq[-1] not in punctuation)):
                split_nodes.append(TextNode(seq, text_type))
            else: 
                split_nodes.append(TextNode(seq, TextNode.text_type_text))
            split_list = []

    return split_nodes

def split_nodes_image(old_nodes):
    img_dict = {}
    split_list = []
    split_nodes = []

    for node in old_nodes:
        if not node.text:
            continue
        if node.text_type != TextNode.text_type_text:
            split_nodes.append(node)
            continue
        lst = extract_markdown_images(node.text)
        if not lst:
            split_nodes.append(node)
            continue
        for tup in lst:
            img_dict[tup[0]] = tup[1]
        split_list.extend(node.text.split("!"))

    for seq in split_list:
        if seq == "":
            continue
        if seq.startswith("["):
            alt_text = seq[1:seq.index("]")]
            split_nodes.append(TextNode(alt_text, TextNode.text_type_image, img_dict[alt_text]))
            after_text = seq[seq.index(")") + 1:]
            if after_text:
                split_nodes.append(TextNode(seq[seq.index(")") + 1:], TextNode.text_type_text))
        else:
            split_nodes.append(TextNode(seq, TextNode.text_type_text))
    
    return split_nodes

def split_nodes_link(old_nodes):
    img_dict = {}
    split_list = []
    split_nodes = []

    for node in old_nodes:
        if not node.text:
            continue
        if node.text_type != TextNode.text_type_text:
            split_nodes.append(node)
            continue
        lst = extract_markdown_links(node.text)
        if not lst:
            split_nodes.append(node)
            continue
        for tup in lst:
            img_dict[tup[0]] = tup[1]
        split_list.extend(node.text.split("["))

    for seq in split_list:
        if seq == "":
            continue
        if "]" in seq:
            alt_text = seq[:seq.index("]")]
            split_nodes.append(TextNode(alt_text, TextNode.text_type_link, img_dict[alt_text]))
            if seq[-1] != ")":
                split_nodes.append(TextNode(seq[seq.index(")") + 1:], TextNode.text_type_text))
        else:
            split_nodes.append(TextNode(seq, TextNode.text_type_text))
    
    return split_nodes

