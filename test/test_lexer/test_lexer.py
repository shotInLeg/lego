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
            'a', 'aA1',  # lname
            '+', '+=',  # loperation
            'if',  # loperator
            'A', 'AbAc', 'Ab(Ac, Ad)', 'Ab<Bc>',  # ltype
            '1', '12', '1_000', '12.14', '"qwerty"'  # lvalue
        ]

        actual = [
            'lkeyword',
            'lname', 'lname',
            'loperation', 'loperation',
            'loperator',
            'ltype', 'ltype', 'ltype', 'ltype',
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

        self.assertEquals(actual, current)
