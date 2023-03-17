import unittest
from lexer import Lexer, Token, TokenType


class TestLexer(unittest.TestCase):
    def test_integer(self):
        source_code = '42'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected = [Token(TokenType.INT, '42')]
        self.assertEqual(tokens, expected)

    def test_float(self):
        source_code = '3.14159'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected = [Token(TokenType.FLOAT, '3.14159')]
        self.assertEqual(tokens, expected)

    def test_identifier(self):
        source_code = 'x'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected = [Token(TokenType.IDENT, 'x')]
        self.assertEqual(tokens, expected)

    def test_operator(self):
        source_code = '+'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected = [Token(TokenType.OP, '+')]
        self.assertEqual(tokens, expected)

    def test_string(self):
        source_code = '"Hello, world!"'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected = [Token(TokenType.STRING, 'Hello, world!')]
        self.assertEqual(tokens, expected)

    def test_keyword(self):
        source_code = 'print'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected = [Token(TokenType.KEYWORD, 'print')]
        self.assertEqual(tokens, expected)


if __name__ == '__main__':
    unittest.main()
