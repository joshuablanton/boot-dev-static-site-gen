from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    test_text = TextNode("Hello There", TextType.LINK, "https://sinnesloschen.io")

    html_dict = {}
    html_dict["href"] = "https://www.google.com"
    html_dict["target"] = "_blank"
    test_html = HTMLNode("a", "I'm a link", None, html_dict)
    
    print(test_text)
    print(test_html)

if __name__ == "__main__":
    main()
