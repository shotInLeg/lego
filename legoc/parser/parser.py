from legoc.lexer.types import *
from legoc.parser.types import *
from .settings import classes_mapping


class Parser(object):
    def parse_file(self, file_ltokens):
        file_instrs = self._split(file_ltokens, LOperator(','))

        result = []
        for instr in file_instrs:
            # Ключевое слово
            if isinstance(instr[0], LKeyword):
                reduced = self.parse_decl(instr)

            # Выражения инициализации
            elif isinstance(instr[0], LModifier) or \
                    isinstance(instr[0], LName) or \
                    isinstance(instr[0], LType):
                reduced = self.parse_init(instr)

            else:
                raise ValueError('Неожиданный элемент `{}` ожидался: `{}`'.format(
                    instr[0],
                    ' или '.join(['Ключевое слово', 'Модификатор', 'Имя'])
                ))

            result.append(reduced)

        return result

    def parse_context(self, ltokens):
        lst = self._split(ltokens, LOperator(';'))

        result = []
        for part in lst:
            exp = self.parse_instr(part)
            result.append(exp)

        child = [x.get() for x in result]
        b = PFBrackets(child)

        return b

    def parse_struct(self):
        pass

    def parse_decl(self, ltokens):
        pass

    def parse_init(self, ltokens):
        modifier_list = []

        # Считали список модификаторов
        i = 0
        while isinstance(ltokens[i], LModifier):
            modifier_list.append(self._get_ptoken(ltokens[i]))
            i += 1

        lvalue_tokens, other = self._split(ltokens[i::], LOperation('='))

        if lvalue_tokens and isinstance(lvalue_tokens[0], LType):
            lvalue = self.parse_type(lvalue_tokens)
        else:
            lvalue = self.parse_exp(lvalue_tokens)

        itype = None
        if isinstance(other[0], LType):
            type_tokens, end = self._cut_type(other)
            other = other[end::]
            self._print_ltokens(type_tokens)
            self._print_ltokens(other)
            itype = self.parse_type(type_tokens)

        value = self.parse_exp(other)

        if isinstance(value, PFBrackets):
            init = PInitFunc(modifier_list, lvalue, itype, value)
        elif isinstance(lvalue, PType):
            init = PInitType(modifier_list, lvalue, itype, value)
        else:
            init = PInitValue(modifier_list, lvalue, itype, value)

        return init

    def parse_instr(self, ltokens):
        if not ltokens:
            raise ValueError('Ожидалось выражение или оператор')

        if isinstance(ltokens[0], LKeyword):
            raise ValueError('Неожиданный токен `{}`'.format(
                ltokens[0]
            ))

        elif isinstance(ltokens[0], LOperator):
            res = self.parse_oper(ltokens)

        else:
            try:
                res = self.parse_init(ltokens)
            except:
                res = self.parse_exp(ltokens)

        return res.get()

    def parse_oper(self, ltoken):
        pass

    def parse_exp(self, ltokens):
        if not ltokens:
            raise ValueError('Ожидалось выражение')

        i = 0
        stack = []
        while i < len(ltokens):
            tkn = ltokens[i]

            if isinstance(tkn, LOpenBracket):
                tkn, end = self.parser_brackets(i, ltokens)
                i = end
            else:
                tkn = self._get_ptoken(tkn)

            stack = self._reduce(stack, tkn)

            i += 1

        if len(stack) != 1:
            raise ValueError('Неизвестная последовательность')
        return stack[0].get()

    def parser_cbrackets(self, start, lexer_tokens):
        brackets, end = self._slice(start, lexer_tokens, LCloseBracket(')'))
        lst = self._split(brackets, LOperator(','))

        result = []
        for part in lst:
            exp = self.parse_exp(part)
            result.append(exp)

        child = result[0].get() if len(result) == 1 else [x.get() for x in result]
        b = PCBrackets(child)

        return b, end

    def parser_sbrackets(self, start, lexer_tokens):
        brackets, end = self._slice(start, lexer_tokens, LCloseBracket(']'))

        if len(brackets) == 1 and brackets[0] == LOperation('='):
            return PStruct([]), end
        elif len(brackets) == 1 and brackets[0] == LOperation(':'):
            return PDict([]), end

        lst = self._split(brackets, LOperator(','))

        result = []
        for part in lst:
            try:
                exp = self.parse_init(part)
            except:
                exp = self.parse_exp(part)
            result.append(exp)

        child = [x.get() for x in result]
        if child and isinstance(child[0], PInit):
            res = PStruct(child)
        elif child and child[0] == LOperation(':'):
            res = PDict(child)
        else:
            res = PSBrackets(child)

        return res, end

    def parser_fbrackets(self, start, lexer_tokens):
        brackets, end = self._slice(start, lexer_tokens, LCloseBracket('}'))
        context = self.parse_context(brackets)

        return context, end

    def parser_brackets(self, start, lexer_tokens):
        obracket = lexer_tokens[start]
        if obracket.str_value == '(':
            return self.parser_cbrackets(start, lexer_tokens)
        elif obracket.str_value == '[':
            return self.parser_sbrackets(start, lexer_tokens)
        elif obracket.str_value == '{':
            return self.parser_fbrackets(start, lexer_tokens)
        return None

    def parse_type(self, ltokens):
        if not isinstance(ltokens[0], LType):
            raise ValueError('Ожидалось имя типа')

        ptype = PSimpleType(ltokens[0].str_value)

        i = 1
        while i < len(ltokens):
            if ltokens[i] == LOpenBracket('('):
                lst, end = self.parser_func_type(i, ltokens)
                ptype = PFuncType(ptype)
                ptype.args = lst
                i = end + 1

            elif ltokens[i] == LOperation('<') and isinstance(ptype, PSimpleType):
                lst, end = self.parser_templ_type(i, ltokens)
                self._print_ltokens(lst)
                ptype = PTemplType(ptype)
                ptype.args = lst
                i = end + 1

            elif ltokens[i] == LOperation('<') and not isinstance(ptype, PSimpleType):
                raise ValueError('Неожиданный токен `{}` ожидался `{}`'.format(
                    ltokens[i],
                    '('
                ))

            else:
                raise ValueError('Неожиданный токен `{}` ожидался `{}`'.format(
                    ltokens[i],
                    ' или '.join(['(', '<'])
                ))
        return ptype

    def parser_func_type(self, start, lexer_tokens):
        brackets, end = self._slice(start, lexer_tokens, LCloseBracket(')'))
        lst = self._split(brackets, LOperator(','))

        result = []
        for part in lst:
            exp = self.parse_type(part)
            result.append(exp)

        return [x.get() for x in result], end

    def parser_templ_type(self, start, lexer_tokens):
        brackets, end = self._slice(start, lexer_tokens, LOperation('>'), True)
        lst = self._split(brackets, LOperation('|'))

        result = []
        for part in lst:
            exp = self.parse_type(part)
            result.append(exp)

        return [x.get() for x in result], end

    # Private
    def _get_ptoken(self, ltoken):
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
        return None

    def _reduce(self, stack, tkn):
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
    def _cut(start, ltokens, end_token):
        left = []
        i = start + 1
        while i < len(ltokens):
            tkn = ltokens[i]
            if tkn == end_token:
                break
            left.append(tkn)
            i += 1

        return left, i

    @staticmethod
    def _slice(start, lexer_tokens, stop_token, triangle=False):
        brackets = []
        i = start + 1
        while i < len(lexer_tokens):
            tkn = lexer_tokens[i]

            if tkn == stop_token and Parser._is_balanced(lexer_tokens, triangle):
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
    def _is_balanced(lexer_tokens, triangle=False):
        brackets = {'()': 0, '[]': 0, '{}': 0, '<>': 0}

        for tkn in lexer_tokens:
            if isinstance(tkn, LBracket) and tkn.pair() in brackets:
                if isinstance(tkn, LOpenBracket):
                    brackets[tkn.pair()] += 1
                else:
                    brackets[tkn.pair()] -= 1

            # Если учитываем треугольные
            if triangle:
                if tkn == LOperation('<'):
                    brackets['<>'] += 1
                elif tkn == LOperation('>'):
                    brackets['<>'] -= 1

        for count in brackets.values():
            if count != 0:
                return False
        return True

    def _cut_type(self, ltokens):
        result = []

        perm_tokens = [
            LOpenBracket('('), LCloseBracket(')'),
            LOperation('<'), LOperation('>'), LOperator(','), LOperation('|')
        ]

        i = 0
        while i < len(ltokens):
            cur = ltokens[i]
            next = ltokens[i+1] if i+1 < len(ltokens) else None

            if not isinstance(cur, LType) and cur not in perm_tokens:
                break

            if cur == LOpenBracket('(') and \
                    not isinstance(next, LType) and \
                    next not in perm_tokens:
                break

            result.append(cur)
            i += 1

        return result, i

    def _print_ltokens(self, ltokens):
        if ltokens is None:
            print('None')
            return

        for ltoken in ltokens:
            print(ltoken, end=', ')
        print()
