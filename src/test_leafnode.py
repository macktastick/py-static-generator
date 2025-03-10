import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print(node)

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node = LeafNode("a", "Hello, world!", { "href": "https://google.com"} )
        print(node)

        self.assertEqual(node.to_html(), "<a href=\"https://google.com\">Hello, world!</a>")        


if __name__ == "__main__":
    unittest.main()