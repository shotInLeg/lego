from legoc.lexer.types import *
from legoc.lexer.settings import regexp, ltypes


class Lexer(object):
    def run(self, filepath):
        tokens = []
        with open(filepath, 'r') as legofile:
            for line in legofile:
                line = line.replace('\n', ' ')
                line = line.replace('\r', ' ')

                token = ''
                for c in line:
                    new_token = token + c
                    token_type = self.get_token_type(new_token)

                    if c == ' ' or token_type is None:
                        tokens.append(self.get_token_type(token))
                        token = c

                    else:
                        token = new_token

        return tokens

    def get_token_type(self, token):
        def max(lst):
            maxI = 0
            for i, item in enumerate(lst):
                if item[1] > lst[maxI][1]:
                    maxI = i
            return lst[maxI]

        token_matches = []
        token_type_name = ''
        for reg in regexp:
            if reg.match(token):
                token_matches.append(regexp[reg])
                token_type_name = max(token_matches)[0]

        if token_type_name:
            return ltypes[token_type_name]
        return None
