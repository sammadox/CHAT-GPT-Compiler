import unittest
from parser import Parser
from code_generator import CodeGenerator


class TestCodeGenerator(unittest.TestCase):
    def test_assignment(self):
        source_code = 'x = 42'
        parser = Parser()
        ast = parser.parse(source_code)
        generator = CodeGenerator(ast)
        code = generator.generate_code()
        expected = 'x = 42'
        self.assertEqual(code, expected)

    def test_print(self):
        source_code = 'print("Hello, world!")'
        parser = Parser()
        ast = parser.parse(source_code)
        generator = CodeGenerator(ast)
        code = generator.generate_code()
        expected = 'print("Hello, world!")'
        self.assertEqual(code, expected)

    def test_expression(self):
        source_code = 'y = 2 * (x + 5)'
        parser = Parser()
        ast = parser.parse(source_code)
        generator = CodeGenerator(ast)
        code = generator.generate_code()
        expected = 'y = (2 * (x + 5))'
        self.assertEqual(code, expected)


if __name__ == '__main__':
    unittest.main()
