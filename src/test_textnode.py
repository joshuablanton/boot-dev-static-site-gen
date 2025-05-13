import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
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


if __name__ == "__main__":
    unittest.main()
