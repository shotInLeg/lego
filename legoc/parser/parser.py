from legoc.lexer.types import *
from legoc.parser.types import *
from legoc.parser.settings import token_mapping


class Parser(object):
    def parser_cbrackets(self, start, lexer_tokens):
        brackets, end = self.slice(start, lexer_tokens, lexer_tokens[start])
        lst = self.split(brackets, LOperator(','))

        result = []
        for part in lst:
            exp = self.parse(part)
            result.append(exp)

        b = PCBrackets()
        b.child = result[0][0].get() if len(result) == 1 else [x[0].get() for x in result]

        return b, end

    def parser_sbrackets(self, start, lexer_tokens):
        brackets, end = self.slice(start, lexer_tokens, lexer_tokens[start])
        lst = self.split(brackets, LOperator(','))

        result = []
        for part in lst:
            exp = self.parse(part)
            result.append(exp)

        b = PList()
        b.child = [x[0].get() for x in result]

        return b, end

    def parser_fbrackets(self, start, lexer_tokens):
        brackets, end = self.slice(start, lexer_tokens, lexer_tokens[start])
        lst = self.split(brackets, LOperator(';'))

        result = []
        for part in lst:
            exp = self.parse(part)
            result.append(exp)

        b = PFBrackets()
        b.child = [x[0].get() for x in result]

        return b, end

    def parser_brackets(self, start, lexer_tokens):
        obracket = lexer_tokens[start]
        if obracket.str_value == '(':
            return self.parser_cbrackets(start, lexer_tokens)
        elif obracket.str_value == '[':
            return self.parser_sbrackets(start, lexer_tokens)
        elif obracket.str_value == '{':
            return self.parser_fbrackets(start, lexer_tokens)
        return None

    def parse(self, lexer_tokens):

        i = 0
        stack = []
        while i < len(lexer_tokens):
            tkn = lexer_tokens[i]

            if isinstance(tkn, LOpenBracket):
                tkn, end = self.parser_brackets(i, lexer_tokens)
                i = end
            else:
                tkn = self.get_token(tkn)

            stack = self.reduce(stack, tkn)

            i += 1

        stack = self.full_reduce(stack)
        '''
        while len(stack) > 1:
            tkn = stack.pop()
            print('stack: {}'.format([str(x) for x in stack]))
            print('tkn: {}'.format(tkn))
            stack = self.reduce(stack, tkn)
        '''

        return stack

    def get_token(self, ltoken):
        for token_type, constr in token_mapping.items():
            if isinstance(ltoken, LOperation):
                if ltoken.str_value == '=':
                    return PInit(ltoken.str_value)
                elif ltoken.str_value in ['!', '~']:
                    return PUOperation(ltoken.str_value)

            if isinstance(ltoken, LOperator):
                if ltoken.str_value == 'if':
                    return PIf(ltoken.str_value)
                else:
                    return POperator(ltoken.str_value)

            if isinstance(ltoken, token_type):
                return constr(ltoken.str_value)
        return None

    def full_reduce(self, stack):
        new_stack = stack[:]

        second = []
        while len(new_stack) > 1:
            size = len(new_stack)
            tkn = new_stack.pop()
            new_stack = self.reduce(new_stack, tkn)

            if len(new_stack) == size:
                second.append(tkn)
                new_stack.pop()
            elif second:
                new_stack.append(second.pop())
        return new_stack

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

    @staticmethod
    def slice(start, lexer_tokens, obracket):
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
    def split(lexer_tokens, token):
        part = []
        result = []
        for tkn in lexer_tokens:
            if tkn == token and Parser.is_balanced(part):
                result.append(part)
                part = []
                continue

            part.append(tkn)

        if part:
            result.append(part)

        return result

    @staticmethod
    def is_balanced(lexer_tokens):
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
