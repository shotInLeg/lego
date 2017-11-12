from copy import copy

from legoc.parser.types.settings import priority
from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.pexpression import PExpression


class PUOperation(BaseParserType):
    def __init__(self, lexeme):
        super(PUOperation, self).__init__()
        self.parents.add(PUOperation.__name__)
        self.str_value = lexeme
        self.pri = priority[lexeme]
        self.complete = False

        self.arg = None

    def get(self):
        return self

    def left_reduce(self, tkn):
        if 'PValue' in tkn.parents:
            result = self
            # Если слева выражение в скобках
            # берем его как аргумент
            if 'PCBrackets' in tkn.parents:
                self.arg = tkn.get()
                self.complete = True

            # Если слева операция с меньшим приоритетом
            # захватываем ее правый аргумент и ставим себя вместо него
            elif 'PBOperation' in tkn.get().parents and tkn.get().pri < self.pri:
                right_tree = copy(tkn.get().right)
                self.arg = right_tree
                self.complete = True
                tkn.get().right = self
                result = tkn.get()

            # Если слева операция с большим или таким же приоритетом
            # берем ее как аргумент
            elif 'PBOperation' in tkn.get().parents and tkn.get().pri >= self.pri:
                self.arg = tkn.get()
                self.complete = True

            else:
                return None

            exp = PExpression()
            exp.child = result
            return exp

        return None

    def right_reduce(self, tkn):
        if 'PValue' in tkn.parents:
            self.arg = tkn.get()
            self.complete = True
        else:
            return None

        exp = PExpression()
        exp.child = self
        return exp

    def __str__(self):
        return '{{{} {}}}'.format(
            self.str_value,
            self.arg
        )
