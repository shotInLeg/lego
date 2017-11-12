from legoc.lexer.types import *
from legoc.parser.types import *


class Parser(object):
    def parse_file(self, file_ltokens):
        self._print_ltokens(file_ltokens)
        return None

    def parse_context(self):
        pass

    def parse_struct(self):
        pass

    # Private
    def _get_ptoken(self, ltoken):
        pass

    def _print_ltokens(self, ltokens):
        for ltoken in ltokens:
            if isinstance(ltoken, LOperator) and ltoken.str_value == ';':
                print(ltoken)
            elif isinstance(ltoken, LOpenBracket) and \
                    (ltoken.str_value == '{' or ltoken.str_value == '['):
                print(ltoken)
            elif isinstance(ltoken, LCloseBracket) and \
                    (ltoken.str_value == '}' or ltoken.str_value == ']'):
                print()
                print(ltoken)
            else:
                print(ltoken, end='')
