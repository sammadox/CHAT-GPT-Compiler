import unittest
from lexer import Lexer, Token, TokenType
from parser import Parser, ASTNode, BinOpNode, UnaryOpNode, NumberNode


class TestParser(unittest.TestCase):
    def test_parse_number(self):
        source_code = '42'
        lexer = Lexer(source_code)
        parser = Parser(lexer)
        ast = parser.parse()
        expected = NumberNode('42')
        self.assertEqual(ast, expected)

    def test_parse_unary_op(self):
        source_code = '-42'
        lexer = Lexer(source_code)
        parser = Parser(lexer)
        ast = parser.parse()
        expected = UnaryOpNode('-', NumberNode('42'))
        self.assertEqual(ast, expected)

    def test_parse_bin_op(self):
        source_code = '3 + 4'
        lexer = Lexer(source_code)
        parser = Parser(lexer)
        ast = parser.parse()
        expected = BinOpNode('+', NumberNode('3'), NumberNode('4'))
        self.assertEqual(ast, expected)

    def test_parse_bin_op_precedence(self):
        source_code = '3 + 4 * 5'
        lexer = Lexer(source_code)
        parser = Parser(lexer)
        ast = parser.parse()
        expected = BinOpNode('+', NumberNode('3'), BinOpNode('*', NumberNode('4'), NumberNode('5')))
        self.assertEqual(ast, expected)

    def test_parse_bin_op_parentheses(self):
        source_code = '(3 + 4) * 5'
        lexer = Lexer(source_code)
        parser = Parser(lexer)
        ast = parser.parse()
        expected = BinOpNode('*', BinOpNode('+', NumberNode('3'), NumberNode('4')), NumberNode('5'))
        self.assertEqual(ast, expected)


if __name__ == '__main__':
    unittest.main()
