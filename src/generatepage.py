from os import path, mkdir, listdir
from shutil import rmtree
from markdownfunctions import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    markdown_file = open(from_path, mode="r")
    markdown = markdown_file.read()
    template_file = open(template_path, mode="r+")
    template = template_file.read()

    contents = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", contents)

    if path.exists(dest_path):
        rmtree(dest_path)
    
    dest = open(dest_path, "x")
    dest.write(template)

    markdown_file.close()
    template_file.close()
    dest.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not path.isfile(dir_path_content):
        if path.exists(dest_dir_path):
            rmtree(dest_dir_path)
        mkdir(dest_dir_path)
        for ext in listdir(dir_path_content):
            generate_pages_recursive(path.join(dir_path_content, ext), template_path, path.join(dest_dir_path, ext))
    else:
        with open(dir_path_content, mode="r") as md, open(template_path, mode="r+") as tmp:
            markdown = md.read()
            content = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            template = tmp.read()
            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", content)

            dest = dest_dir_path.replace("md", "html")
            if path.exists(dest):
                rmtree(dest)

            dest = open(dest, "x")
            dest.write(template)