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
            LNameType('a'), LOperationType('+'), LValueType('5'),
            LNameType('b'), LOperationType('+'), LValueType('6')
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
            LOpenBracketType('('), LCloseBracketType(')'),
            LOpenBracketType('{'), LCloseBracketType('}'),
            LOpenBracketType('['), LCloseBracketType(']'),
            LOperationType('<'), LOperationType('>')
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
            LValueType('1'), LValueType('1.'), LValueType('12'),
            LValueType('1.2'), LValueType('123'), LValueType('12.3'),
            LValueType('12.34'), LValueType('1_000'),
            LValueType('1_000.23'), LValueType('1.000_23'),
            LValueType('1_000.000_23')
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
            LTypeType('A'), LTypeType('Ab'), LTypeType('A1'),
            LTypeType('Ab1'), LTypeType('T_A'), LTypeType('T_A1'),
            LTypeType('T_1A'), LTypeType('T_Ab'), LTypeType('T_Ab1')
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
            LOperatorType('if'), LOperatorType('elif'), LOperatorType('else'),
            LOperatorType('while'), LOperatorType('do'), LOperatorType('for'),
            LOperatorType('with'), LOperatorType('throw'),
            LOperatorType('try'), LOperatorType('catch'),
            LOperatorType('finally'), LOperatorType('return'),
            LOperatorType(','), LOperatorType(';')
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
            LOperationType('+'), LOperationType('-'), LOperationType('*'),
            LOperationType('/'), LOperationType('%'),  LOperationType('++'),
            LOperationType('--'), LOperationType('+='),  LOperationType('-='),
            LOperationType('*='), LOperationType('/='),  LOperationType('%='),
            LOperationType('++='), LOperationType('--='),  LOperationType('<'),
            LOperationType('>'), LOperationType('<='),  LOperationType('>='),
            LOperationType('=='), LOperationType('!='), LOperationType('!'),
            LOperationType('.'), LOperationType('->'), LOperationType('in'),
            LOperationType('is'), LOperationType('=')
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
            LNameType('a'), LNameType('aa'), LNameType('aBcDe'),
            LNameType('a1'), LNameType('r2d2'), LNameType('r2D2')
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
            LKeywordType('cnst'), LKeywordType('priv'),
            LKeywordType('prot'), LKeywordType('publ'),
            LKeywordType('read'), LKeywordType('write'),
            LKeywordType('clr')
        ]

        lexer = Lexer()
        current_data = lexer.run(test_data_file)

        for token in current_data:
            print(token)
        print()

        self.assertEqual(len(actual_data), len(current_data), 'Invalid size')
        for act, cur in zip(actual_data, current_data):
            self.assertEqual(act, cur, '{} != {}'.format(act, cur))
