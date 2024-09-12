from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_list = []
    split_nodes = []

    for node in old_nodes:
        if node.text_type != TextNode.text_type_text:
            split_nodes.append(node)

        split_list.extend(node.text.split(delimiter))

    print(split_list)

    for seq in split_list:
        if not seq:
            continue
        if seq[0] != " " and seq[-1] !=  " ":
            split_nodes.append(TextNode(seq, text_type))
        else: 
            split_nodes.append(TextNode(seq, TextNode.text_type_text))

    return split_nodes
