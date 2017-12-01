from copy import copy

from legoc.lexer.types import *
from legoc.parser.types import *
from .settings import classes_mapping


class BaseParser(object):
    def get_ptoken(self, ltoken):
        for token_type, constr in classes_mapping.items():
            if isinstance(ltoken, LOperation):
                if ltoken.str_value in POperation.un:
                    return PUnOperation(ltoken.str_value)
                elif ltoken.str_value in POperation.bin:
                    return PBinOperation(ltoken.str_value)
                else:
                    raise ValueError('Неизвестная операция `{}`'.format(ltoken))

            if isinstance(ltoken, token_type):
                return constr(ltoken.str_value)

        raise ValueError('Неизвестный токен `{}`'.format(
            ltoken
        ))

    def reduce(self, stack, tkn):
        new_stack = stack[:]
        if not new_stack:
            new_stack.append(tkn)
            return new_stack

        prev = new_stack.pop()

        # print('{}.right_reduce({})'.format(prev, tkn))
        right = prev.right_reduce(tkn)
        if right is not None:
            new_stack.append(right)
            return new_stack

        # print('{}.left_reduce({})'.format(tkn, prev))
        left = tkn.left_reduce(prev)
        if left is not None:
            new_stack.append(left)
            return new_stack

        new_stack.extend([prev, tkn])
        return new_stack

    def from_brackets(self, tokens, end_bracket, spliter):
        brackets, end = self.cut_on_token(tokens, end_bracket, 1)
        lst = self.split(brackets, spliter)

        return lst, end

    def cut_range(self, tokens, start, end):
        result = []

        i = start
        while i < len(tokens) and i <= end:
            result.append(tokens[i])
            i += 1

        return result, i

    def cut_on_token(self, tokens, stop_token, start=0):
        result = []

        i = start
        while i < len(tokens):
            tkn = tokens[i]
            if tkn == stop_token and self.is_balanced(result):
                break
            result.append(tkn)
            i += 1

        return result, i

    def split(self, tokens, token):
        part = []
        result = []

        for tkn in tokens:
            if tkn == token and self.is_balanced(part):
                result.append(part)
                part = []
                continue
            part.append(tkn)

        if part:
            result.append(part)

        return result

    def replace(self, tokens, token, new_token):
        result = []

        for tkn in tokens:
            if tkn == token and self.is_balanced(result):
                result.append(new_token)
            else:
                result.append(tkn)

        return result

    def is_balanced(self, tokens):
        brackets = {'()': 0, '[]': 0, '{}': 0, '<>': 0,
                    'for': 0, 'with': 0}

        operator = ''
        for tkn in tokens:
            if isinstance(tkn, LOpenBracket) and tkn.pair() in brackets:
                brackets[tkn.pair()] += 1
                if tkn.pair() == '{}' and operator:
                    brackets[operator] -= 1
                    operator = ''

            elif isinstance(tkn, LCloseBracket) and tkn.pair() in brackets:
                brackets[tkn.pair()] -= 1

            elif isinstance(tkn, LOperator) and tkn.str_value in brackets:
                operator = tkn.str_value
                brackets[operator] += 1

        for count in brackets.values():
            if count != 0:
                return False
        return True

    def is_in(self, tokens, token):
        last = []
        for tkn in tokens:
            if tkn == token and self.is_balanced(last):
                return True
            last.append(tkn)
        return False

    def print(self, tokens):
        if tokens is None:
            print('None')
            return

        for tkn in tokens:
            print(tkn, end=', ')
        print()
