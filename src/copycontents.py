from os import *
from shutil import copy
from shutil import rmtree

def copy_contents(file_path):    
    public_path = file_path.replace("./static", "./public")
    print(public_path)
    
    if not path.isfile(file_path):
        if path.exists(public_path):
            rmtree(public_path)
        mkdir(public_path)
        for ext in listdir(file_path):
            copy_contents(path.join(file_path, ext))
    else:
        copy(file_path, public_path)
