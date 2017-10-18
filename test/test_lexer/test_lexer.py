import os

from unittest import TestCase
from legoc.lexer.settings import regexp
from legoc.lexer.lexer import Lexer
from legoc.lexer.types import *


class TestLexer(TestCase):
    def test_regexp(self):
        def max(lst):
            maxI = 0
            for i, item in enumerate(lst):
                if item[1] > lst[maxI][1]:
                    maxI = i
            return lst[maxI]

        dataset = [
            'let',  # lkeyword
            'a', 'aA1',  # lname
            '+', '+=',  # loperation
            'if',  # loperator
            'A', 'AbAc', 'Ab(Ac, Ad)', 'Ab<Bc>',  # ltype
            '(', ')', '{', '}', '[', ']', '<', '>',  # lbracket
            '1', '12', '1_000', '12.14', '"qwerty"'  # lvalue
        ]

        actual = [
            'lkeyword',
            'lname', 'lname',
            'loperation', 'loperation',
            'loperator',
            'ltype', 'ltype', 'ltype', 'ltype',
            'lopen_bracket', 'lclose_bracket', 'lopen_bracket', 'lclose_bracket',
            'lopen_bracket', 'lclose_bracket', 'loperation', 'loperation',
            'lvalue', 'lvalue', 'lvalue', 'lvalue', 'lvalue'
        ]

        current = []
        for i, item in enumerate(dataset):
            current.append('lexername')
            item_matches = []
            for reg in regexp:
                if reg.match(item):
                    item_matches.append(regexp[reg])
                    current[i] = max(item_matches)[0]

        self.assertEqual(actual, current)

    def test_lexer_run(self):
        actual = {
            os.path.join(
                os.path.dirname(__file__),
                'lexer_run_test_files',
                'test_spaces.txt'
            ): [
                LNameType('a'), LOperationType('+'), LValueType('5'),
                LNameType('b'), LOperationType('+'), LValueType('6')
            ],

            os.path.join(
                os.path.dirname(__file__),
                'lexer_run_test_files',
                'test_brackets.txt'
            ): [
                LOpenBracketType('('), LCloseBracketType(')'),
                LOpenBracketType('{'), LCloseBracketType('}'),
                LOpenBracketType('['), LCloseBracketType(']'),
                LOperationType('<'),LOperationType('>'),
                LOpenBracketType('('), LCloseBracketType(')'),
                LOpenBracketType('{'), LCloseBracketType('}'),
                LOpenBracketType('['), LCloseBracketType(']'),
                LOperationType('<'), LOperationType('>'),
                LOpenBracketType('('), LCloseBracketType(')'),
                LOpenBracketType('{'), LCloseBracketType('}'),
                LOpenBracketType('['), LCloseBracketType(']'),
                LOperationType('<'), LOperationType('>'),
            ]
        }

        lexer = Lexer()
        for test_file in actual:
            tokens = lexer.run(test_file)
            self.assertEqual(len(actual[test_file]), len(tokens), 'Invalid size')
            for act, cur in zip(actual[test_file], tokens):
                self.assertEqual(act, cur, '{} != {}'.format(act, cur))
