import os

from unittest import TestCase
from legoc.lexer.lexer import Lexer
from legoc.parser.parser import Parser
from legoc.parser.types import *


class TestParser(TestCase):
    def test_with(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_with.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_dowhile(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_dowhile.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_while(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_while.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_for(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_for.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_expressions(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_expressions.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_function(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_function.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_vector(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_vector.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_struct(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_struct.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()

    def test_dict(self):
        test_data_file = os.path.join(
            os.path.dirname(__file__),
            'parser_run_test_files',
            'test_dict.txt'
        )

        lexer = Lexer()
        ltokens = lexer.run(test_data_file)

        parser = Parser()
        ptokens = parser.parse_file(ltokens)

        for token in ptokens:
            print(token)
        print()
