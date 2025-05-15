import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click Here!</a>")

    def test_leaf_to_html_a_mult_props(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click Here!</a>")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text")
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</p>"
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("span", None)
        self.assertRaises(ValueError, parent_node.to_html)
    
    def test_to_html_with_nested_parents(self):
        grandchild_node = LeafNode("b", "Bold Text")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("span", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<span><div><b>Bold Text</b></div></span>"
        )

if __name__ == "__main__":
    unittest.main()
