from textnode import TextNode, TextType

def main():
    test_text = TextNode("Hello There", TextType.LINK, "https://sinnesloschen.io")

    print(test_text)

if __name__ == "__main__":
    main()
