from legoc.lexer.types import *
from legoc.parser.types import *


class Parser(object):
    def parse_file(self, file_ltokens):
        file_instrs = self._split(file_ltokens, LOperator(','))
        for instr in file_instrs:
            for token in instr:
                print(token, end=' ')
            print()
        print()
        return None

    def parse_context(self):
        pass

    def parse_struct(self):
        pass

    # Private
    def _get_ptoken(self, ltoken):
        pass

    @staticmethod
    def _slice(start, lexer_tokens, obracket):
        brackets = []
        i = start + 1
        while i < len(lexer_tokens):
            tkn = lexer_tokens[i]
            if isinstance(tkn, LCloseBracket) and \
                            tkn.current_number == obracket.current_number:
                break
            brackets.append(tkn)

            i += 1

        return brackets, i

    @staticmethod
    def _split(lexer_tokens, token):
        part = []
        result = []
        for tkn in lexer_tokens:
            if tkn == token and Parser._is_balanced(part):
                result.append(part)
                part = []
                continue

            part.append(tkn)

        if part:
            result.append(part)

        return result

    @staticmethod
    def _is_balanced(lexer_tokens):
        brackets = {'()': 0, '[]': 0, '{}': 0}

        for tkn in lexer_tokens:
            if isinstance(tkn, LBracket) and tkn.pair() in brackets:
                if isinstance(tkn, LOpenBracket):
                    brackets[tkn.pair()] += 1
                else:
                    brackets[tkn.pair()] -= 1

        for count in brackets.values():
            if count != 0:
                return False
        return True

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


