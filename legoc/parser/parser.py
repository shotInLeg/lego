from legoc.lexer.types import *
from legoc.parser.types import *
from .base_parser import BaseParser


class Parser(BaseParser):
    def parse_file(self, file_ltokens):
        file_instrs = self.split(file_ltokens, LOperator(','))

        result = []
        for instr in file_instrs:
            # Ключевое слово
            if isinstance(instr[0], LKeyword):
                reduced = self.parse_decl(instr)

            # Выражения инициализации
            elif isinstance(instr[0], LModifier) or \
                    isinstance(instr[0], LName) or \
                    isinstance(instr[0], LType):

                if self.is_in(instr, LOperation('=')) or \
                        self.is_in(instr, LOperation('=>')):
                    reduced = self.parse_init(instr)
                else:
                    raise ValueError('Ожидалось объявление')

            else:
                raise ValueError('Неожиданный элемент `{}` ожидался: `{}`'.format(
                    instr[0],
                    ' или '.join(
                        ['Ключевое слово', 'Модификатор', 'Имя', 'Имя типа']
                    )
                ))

            result.append(reduced)

        return result

    def parse_init_list(self, tokens):
        file_instrs = self.split(tokens, LOperator(','))

        result = []
        for instr in file_instrs:
            # Выражения инициализации
            if isinstance(instr[0], LModifier) or \
                    isinstance(instr[0], LName) or \
                    isinstance(instr[0], LType):

                if self.is_in(instr, LOperation('=')) or \
                        self.is_in(instr, LOperation('=>')):
                    reduced = self.parse_init(instr)
                else:
                    raise ValueError('Ожидалось объявление')

            else:
                raise ValueError('Неожиданный элемент `{}` ожидался: `{}`'.format(
                    instr[0],
                    ' или '.join(
                        ['Ключевое слово', 'Модификатор', 'Имя', 'Имя типа']
                    )
                ))

            result.append(reduced)

        return result

    def parse_decl(self, ltokens):
        # Обработка ключевых слов
        return None

    def parse_init(self, tokens):
        # publ a = 5, list.get(5) = 7 + 9
        if self.is_in(tokens, LOperation('=')):
            return self.parse_init_value(tokens)

        # sum(a|Int, b|Int) => Int { a + b }
        elif self.is_in(tokens, LOperation('=>')):
            return self.parse_def_func(tokens)

        else:
            raise ValueError('Ожидалась инструкция инициализации: `{}`'.format(
                ' '.join([str(x) for x in tokens])
            ))

    def parse_init_value(self, tokens):
        modifiers, i = self.parse_modifiers(tokens)
        lvalue_tokens, value_tokens = self.split(tokens[i::], LOperation('='))
        lvalue = self.parse_exp(lvalue_tokens)
        value = self.parse_exp(value_tokens)

        # MyList<T_1>(Parent) = [ ... ]
        if isinstance(lvalue, PType) or \
                (isinstance(lvalue, POperation) and isinstance(lvalue.left, PType)):
            init = PInitType(modifiers, lvalue, value)

        # a = 5, list.get(x) = 8
        else:
            init = PInitValue(modifiers, lvalue, value)

        return init

    def parse_def_func(self, tokens):
        modifiers, i = self.parse_modifiers(tokens)
        lvalue_tokens, type_value_tokens = self.split(
            tokens[i::], LOperation('=>')
        )
        type_tokens, end = self.cut_on_token(
            type_value_tokens, LOpenBracket('{')
        )
        value_tokens = type_value_tokens[end::]

        lvalue = self.parse_exp(lvalue_tokens)
        return_type = self.parse_exp(type_tokens) if type_tokens else None
        value = self.parse_exp(value_tokens)

        return PInitFunc(modifiers, lvalue, return_type, value)

    def parse_modifiers(self, tokens):
        modifiers = []
        for i, tkn in enumerate(tokens):
            if isinstance(tkn, LModifier):
                modifiers.append(self.get_ptoken(tkn))
            else:
                return modifiers, i
        return modifiers, len(tokens)

    def parse_exp(self, tokens):
        if not tokens:
            raise ValueError('Ожидалось выражение')

        i = 0
        stack = []
        while i < len(tokens):
            tkn = tokens[i]

            # (5 + 6)
            if isinstance(tkn, LOpenBracket):
                tkn, end = self.parser_brackets(i, tokens)
                i = end
            else:
                try:
                    tkn = self.get_ptoken(tkn)
                except:
                    pass

            try:
                stack = self.reduce(stack, tkn)

            except Exception as ex:
                raise ValueError('{}: reduce(stack={}, tkn={})'.format(
                    ex, [str(x) for x in stack], tkn
                ))
            i += 1

        if len(stack) != 1:
            raise ValueError('Неизвестная последовательность {}'.format(
                ' '.join([str(x.get()) for x in stack])
            ))

        try:
            temp = stack[0].get()
        except Exception as ex:
            pass
        return stack[0].get()

    def parse_instr(self, tokens):
        if not tokens:
            raise ValueError('Ожидалось выражение или оператор')

        # if a > b { ... }
        if isinstance(tokens[0], LOperator):
            res = self.parse_oper(tokens)

        # a = 5, fib(n|Int) => Int { ... }
        elif self.is_in(tokens, LOperation('=')) or \
                    self.is_in(tokens, LOperation('=>')):
            res = self.parse_init(tokens)

        # max(a, b) + 7
        else:
            res = self.parse_exp(tokens)

        return res.get()

    def parse_oper(self, ltoken):
        if not ltoken or not isinstance(ltoken[0], LOperator):
            raise ValueError('Ожидался оператор {}'.format(
                ltoken
            ))

        if ltoken[0].str_value == 'return':
            exp = self.parse_exp(ltoken[1::])
            return PReturn(exp)

        elif ltoken[0].str_value == 'if':
            return self.parse_if(ltoken)

        elif ltoken[0].str_value == 'while':
            return self.parse_while(ltoken)

        elif ltoken[0].str_value == 'for':
            return self.parse_for(ltoken)

        elif ltoken[0].str_value == 'do':
            return self.parse_dowhile(ltoken)

        elif ltoken[0].str_value == 'with':
            return self.parse_with(ltoken)

        elif ltoken[0].str_value == 'try':
            return self.parse_try(ltoken)

    def parse_if(self, tokens):
        cond_cntxts = self.split(tokens[1::], LOperator('elif'))

        pif = None
        for i, cond_cntx in enumerate(cond_cntxts):
            cond_tokens, end = self.cut_on_token(
                cond_cntx, LOpenBracket('{')
            )
            cntx_tokens = cond_cntx[end::]

            if self.is_in(cond_tokens, LOperator('else')):
                cntx = self.parse_exp(cntx_tokens)
                pelse = PElse(cntx)
                pif = pif.add(pelse)
                break

            cond = self.parse_exp(cond_tokens)
            cntx = self.parse_exp(cntx_tokens)

            if i == 0:
                pif = PIf(cond, cntx)
                continue

            pelif = PElif(cond, cntx)
            pif.add(pelif)

        return pif.get()

    def parse_while(self, tokens):
        cond_tokens, end = self.cut_on_token(tokens, LOpenBracket('{'), 1)
        cntx_tokens = tokens[end::]
        cond = self.parse_exp(cond_tokens)
        context = self.parse_exp(cntx_tokens)
        return PWhile(cond, context)

    def parse_for(self, tokens):
        cond_tokens, end = self.cut_on_token(tokens, LOpenBracket('{'), 1)
        cntx_tokens = tokens[end::]

        cond_tokens = self.split(cond_tokens, LOperator(';'))
        context = self.parse_exp(cntx_tokens)

        # for x in arr { ... }
        if len(cond_tokens) == 1:
            cond = self.parse_exp(cond_tokens[0])
            return PForEach(cond, context)

        # for i = 0; i < N; i += 1 { ... }
        elif len(cond_tokens) == 3:
            start_tokens, cond_tokens, step_tokens = cond_tokens
            start = self.parse_init_list(start_tokens)
            cond = self.parse_exp(cond_tokens)
            steps = [self.parse_exp(x) for x in self.split(step_tokens, LOperator(','))]
            return PFor(start, cond, steps, context)

        else:
            raise ValueError('Неизветный список параметров цикла for `{}`'.format(
                [str(x) for x in cond.child]
            ))

    def parse_dowhile(self, tokens):
        context_tokens, cond_tokens = self.split(tokens[1::], LOperator('while'))
        context = self.parse_exp(context_tokens)
        cond = self.parse_exp(cond_tokens)

        return PDoWhile(cond, context)

    def parse_with(self, tokens):
        exp_tokens, end = self.cut_on_token(tokens, LOpenBracket('{'), 1)
        cntx_tokens = tokens[end::]
        exp = self.parse_exp(exp_tokens)
        context = self.parse_exp(cntx_tokens)

        if isinstance(exp, PCBrackets):
            return PWith(exp.get_list(), context)
        else:
            return PWith([exp.get()], context)

    def parse_try(self, tokens):
        cond_cntxts = self.split(tokens[1::], LOperator('catch'))

        have_finally = False
        if self.is_in(cond_cntxts[-1], LOperator('finally')):
            last = cond_cntxts.pop(-1)
            parts = self.split(last, LOperator('finally'))
            cond_cntxts.extend(parts)
            have_finally = True

        ptry = None
        for i, part in enumerate(cond_cntxts):
            # try { ... }
            if i == 0:
                cntx = self.parse_exp(part)
                ptry = PTry(cntx)
                continue

            # finally { ... }
            if i == len(cond_cntxts)-1 and have_finally:
                cntx = self.parse_exp(part)
                pfinally = PFinally(cntx)
                ptry.add(pfinally)
                break

            # catch( ... ) { ... }
            params_tokens, end = self.cut_on_token(part, LOpenBracket('{'))
            context_tokens = part[end::]

            params = self.parse_exp(params_tokens)
            context = self.parse_exp(context_tokens)

            pcatch = PCatch(params, context)
            ptry.add(pcatch)

        return ptry.get()

    def parser_cbrackets(self, start, tokens):
        from_brackets, end = self.from_brackets(
            tokens[start::], LCloseBracket(')'), LOperator(',')
        )
        exps = [self.parse_exp(exp) for exp in from_brackets]

        child = exps[0].get() if len(exps) == 1 else [x.get() for x in exps]
        b = PCBrackets(child)

        return b, start+end

    def parser_tbrackets(self, start, tokens):
        from_brackets, end = self.from_brackets(
            tokens[start::], LCloseBracket('>'), LOperator(',')
        )
        exps = [self.parse_exp(exp) for exp in from_brackets]

        child = [x.get() for x in exps]
        context = PTBrackets(child)

        return context, start+end

    def parser_fbrackets(self, start, tokens):
        from_brackets, end = self.from_brackets(
            tokens[start::], LCloseBracket('}'), LOperator(';')
        )
        instrs = [self.parse_instr(ins) for ins in from_brackets]

        child = [x.get() for x in instrs]
        context = PFBrackets(child)

        return context, start+end

    def parser_sbrackets(self, start, tokens):
        from_brackets, end = self.from_brackets(
            tokens[start::], LCloseBracket(']'), LOperator(',')
        )

        # [=] Пустая структура
        if len(from_brackets) == 1 and from_brackets[0] == [LOperation('=')]:
            return PStruct([]), end

        # [:] Пустой словарь
        elif len(from_brackets) == 1 and from_brackets[0] == [LOperation(':')]:
            return PDict([]), end

        # [] Пустой список
        elif not from_brackets:
            return PList([]), end

        result = []
        for part in from_brackets:
            if self.is_in(part, LOperation('=')) or \
                    self.is_in(part, LOperation('=>')):
                exp = self.parse_init(part)
            else:
                exp = self.parse_exp(part)
            result.append(exp)

        child = [x.get() for x in result]

        # [ a = 5, b = 6 ] Стуктура
        if child and isinstance(child[0], PInit):
            res = PStruct(child)

        # [ "q": "w", "e": "r" ] Словарь
        elif child and isinstance(child[0], PBinOperation) and child[0].str_value == ':':
            res = PDict(child)

        # [1, 2, 3, "adasd", 4] Списое
        else:
            res = PList(child)

        return res, start+end

    def parser_brackets(self, start, tokens):
        obracket = tokens[start]
        if obracket.str_value == '(':
            return self.parser_cbrackets(start, tokens)
        elif obracket.str_value == '[':
            return self.parser_sbrackets(start, tokens)
        elif obracket.str_value == '{':
            return self.parser_fbrackets(start, tokens)
        elif obracket.str_value == '<':
            return self.parser_tbrackets(start, tokens)

        raise ValueError('Ожидалась скобка `{}`'.format(
            obracket
        ))
