from copycontents import *
from generatepage import *

def main():
    generate_pages_recursive("./content", "./template.html", "./public")
    copy_contents("./static")

if __name__ == "__main__":
    main()