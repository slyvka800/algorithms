import unittest
from main import search

class TestBoyerMoore(unittest.TestCase):
    def test_search(self):

        pattern = "each"
        text = "assume each iteration happens"
        output = ["Found \"each\" in \"assume each iteration happens\""]
        self.assertEqual(search(pattern, text), output)

        pattern = "offfset"
        text = "The arbitrary offset you’ll use to animate the auxiliary label"
        output = ["Not found \"offfset\" in \"The arbitrary offset you’ll use to animate the auxiliary label\""]
        self.assertEqual(search(pattern, text), output)

        pattern = "ab"
        text = "abababab sdjsdjsdks sdisjis ab ab"
        output = ["Found \"ab\" in \"abababab sdjsdjsdks sdisjis ab ab\"",
                  "Found \"ab\" in \"abababab sdjsdjsdks sdisjis ab ab\"",
                  "Found \"ab\" in \"abababab sdjsdjsdks sdisjis ab ab\"",
                  "Found \"ab\" in \"abababab sdjsdjsdks sdisjis ab ab\"",
                  "Found \"ab\" in \"abababab sdjsdjsdks sdisjis ab ab\"",
                  "Found \"ab\" in \"abababab sdjsdjsdks sdisjis ab ab\""]
        self.assertEqual(search(pattern, text), output)

