import os

from unittest import TestCase
from legoc.lexer.settings import regexp
from legoc.lexer.lexer import Lexer
from legoc.lexer.types import *


class TestLexer(TestCase):
    def test_spaces(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_spaces.txt'
        )

        actual_data = [
            LName('a'), LOperation('+'), LConstant('5'),
            LName('b'), LOperation('+'), LConstant('6')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_bracket(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_brackets.txt'
        )

        actual_data = [
            LOpenBracket('('), LCloseBracket(')'),
            LOpenBracket('{'), LCloseBracket('}'),
            LOpenBracket('['), LCloseBracket(']'),
            LOperation('<'), LOperation('>')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_value(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_values.txt'
        )

        actual_data = [
            LConstant('1'), LConstant('1.'), LConstant('12'),
            LConstant('1.2'), LConstant('123'), LConstant('12.3'),
            LConstant('12.34'), LConstant('1_000'),
            LConstant('1_000.23'), LConstant('1.000_23'),
            LConstant('1_000.000_23')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_types(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_types.txt'
        )

        actual_data = [
            LType('A'), LType('Ab'), LType('A1'),
            LType('Ab1'), LType('T_A'), LType('T_A1'),
            LType('T_1A'), LType('T_Ab'), LType('T_Ab1')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_operators(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_operators.txt'
        )

        actual_data = [
            LOperator('if'), LOperator('elif'), LOperator('else'),
            LOperator('while'), LOperator('do'), LOperator('for'),
            LOperator('with'), LOperator('throw'),
            LOperator('try'), LOperator('catch'),
            LOperator('finally'), LOperator('return'),
            LOperator(','), LOperator(';')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_operations(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_operations.txt'
        )

        actual_data = [
            LOperation('+'), LOperation('-'), LOperation('*'),
            LOperation('/'), LOperation('%'),  LOperation('++'),
            LOperation('--'), LOperation('+='),  LOperation('-='),
            LOperation('*='), LOperation('/='),  LOperation('%='),
            LOperation('++='), LOperation('--='),  LOperation('<'),
            LOperation('>'), LOperation('<='),  LOperation('>='),
            LOperation('=='), LOperation('!='), LOperation('!'),
            LOperation('.'), LOperation('->'), LOperation('in'),
            LOperation('is'), LOperation('=')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_names(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_names.txt'
        )

        actual_data = [
            LName('a'), LName('aa'), LName('aBcDe'),
            LName('a1'), LName('r2d2'), LName('r2D2')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))

    def test_keywords(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'lexer_run_test_files',
            'test_keywords.txt'
        )

        actual_data = [
            LKeyword('cnst'), LKeyword('priv'),
            LKeyword('prot'), LKeyword('publ'),
            LKeyword('read'), LKeyword('write'),
            LKeyword('clr')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))
