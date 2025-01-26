from textnode import TextNode, TextType


def main():
    obj = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(obj)
if __name__ == "__main__":
    main()