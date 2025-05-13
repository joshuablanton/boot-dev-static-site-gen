import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        html_dict = {}
        html_dict["href"] = "https://www.google.com"
        html_dict["target"] = "_blank"
        test_html = HTMLNode("a", "I'm a link", None, html_dict)
        node = HTMLNode("a", "I'm a link", None, html_dict)
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        html_dict = {}
        html_dict["href"] = "https://www.google.com"
        html_dict["target"] = "_blank"
        test_html = HTMLNode("a", "I'm a link", None, html_dict)
        test_case = test_html.props_to_html()
        test_text = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(test_case, test_text)

    def test_repr(self):
        node = HTMLNode("b", "Hello There")
        test_text = "HTMLNode(b, Hello There, None, None)"
        self.assertEqual(str(node), test_text)


if __name__ == "__main__":
    unittest.main()
