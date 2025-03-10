import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_blank_children(self):
        print("Working on HTML Node")
        props = { "href": "https://google.com" }
        node = HTMLNode("a", "link to google", None, props)
        self.assertEqual(node.children, None)

    def test_props_to_html(self):
        url = "https://google.com"
        props = { "href": url }
        node = HTMLNode("a", "link to google", None, props)
        html = node.props_to_html()
        comp = f" href=\"{url}\""
        self.assertEqual(html, comp)

    def test_repr(self):
        props = { "href": "https://google.com" }
        node = HTMLNode("a", "link to google", None, props)
        comp = "HTMLNode(a, link to google, None, {'href': 'https://google.com'})"
        self.assertEqual(node.__repr__(), comp)        

if __name__ == "__main__":
    unittest.main()
