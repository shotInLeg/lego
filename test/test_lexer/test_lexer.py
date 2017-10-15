from unittest import TestCase
from legoc.lexer.settings import regexp


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

            'a',  # lname
            'aA1',  # lname

            '+',  # loperation
            '+=',  # loperation

            'if',  # loperator

            'A',  # ltype
            'AbAc',  # ltype
            'Ab(Ac, Ad)',  # ltype
            'Ab<Bc>',  # ltype

            '1',  # lvalue
            '12',  # lvalue
            '1_000',  # lvalue
            '12.14',  # lvalue
            '"qwerty"'  # lvalue
        ]

        actual = [
            'lkeyword'
            'lname',
            'lname',
            'loperation',
            'loperation',
            'loperator',
            'ltype',
            'ltype',
            'ltype',
            'ltype',
            'lvalue',
            'lvalue',
            'lvalue',
            'lvalue',
            'lvalue',
        ]

        current = []
        for i, item in enumerate(dataset):
            current.append(('lexername', 0))
            item_matches = []
            for reg in regexp:
                if reg.match(item):
                    item_matches.append(regexp[reg])
                    current[i] = max(item_matches)[0]

        self.assertEqual(actual, current)
