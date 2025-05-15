import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_neq_with_url(self):
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is some anchor text", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_img_text_node_to_html_node(self):
        node = TextNode("A Cute Cat", TextType.IMAGE, "https://miro.medium.com/v2/resize:fit:1080/0*A7MUqyCLvZDcHkfM.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://miro.medium.com/v2/resize:fit:1080/0*A7MUqyCLvZDcHkfM.jpg", "alt": "A Cute Cat"})

    def test_invalid_text_node_to_html_node(self):
        node = TextNode("This shouldn't work", "Invalid")
        self.assertRaises(Exception, text_node_to_html_node, node)
    
    def test_code_text_node_to_html_node(self):
        node = TextNode("hack the gibson.", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "hack the gibson.")

if __name__ == "__main__":
    unittest.main()
