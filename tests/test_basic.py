import unittest
from usc.model import Symbol, USCDocument
from usc.parser import USCParser
from usc.resolver import USCResolver
from usc.payload import PayloadHandler

class TestUSC(unittest.TestCase):
    def setUp(self):
        self.parser = USCParser()

    def test_parse_simple_symbol(self):
        text = """@symbol test
@mode inline
@type text/plain
@data <<
hello
>>

content test"""
        doc = self.parser.parse(text)
        self.assertIn("test", doc.symbols)
        self.assertEqual(doc.symbols["test"].data, "hello")
        self.assertIn("content test", doc.raw_content)

    def test_resolve_inline(self):
        text = """@symbol foo
@mode inline
@type text/plain
@data <<
BAR
>>

This is foo."""
        doc = self.parser.parse(text)
        resolver = USCResolver(doc)
        result = resolver.resolve_all()
        # The parser might leave newlines in raw_content depending on implementation
        # But verify 'foo' is replaced by 'BAR'
        self.assertIn("This is BAR.", result)

    def test_symbolic_mode(self):
        text = """@symbol var
@mode symbolic

Value: var"""
        doc = self.parser.parse(text)
        resolver = USCResolver(doc)
        result = resolver.resolve_all()
        self.assertIn("Value: var", result)

    def test_multiple_symbols(self):
        text = """@symbol a
@mode inline
@data <<
A
>>
@symbol b
@mode inline
@data <<
B
>>

a and b"""
        doc = self.parser.parse(text)
        resolver = USCResolver(doc)
        result = resolver.resolve_all()
        self.assertIn("A and B", result)

if __name__ == '__main__':
    unittest.main()
