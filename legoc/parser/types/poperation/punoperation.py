from copy import copy

from legoc.parser.types.poperation.poperation import POperation
from legoc.parser.types.pexp.pexpression import PExpression


class PUnOperation(POperation):
    def __init__(self, lexeme):
        super(PUnOperation, self).__init__(lexeme)
        self.tstack.append(PUnOperation.__name__)

        self.pri = self.priority[lexeme]
        self.arg = None

    def get(self):
        return self

    def left_reduce(self, tkn):
        if 'PValue' in tkn.tstack:
            result = self
            # Если слева выражение в скобках
            # берем его как аргумент
            if 'PCBrackets' in tkn.tstack:
                self.arg = tkn.get()
                self.complete = True

            # Если слева операция с меньшим приоритетом
            # захватываем ее правый аргумент и ставим себя вместо него
            elif 'PBinOperation' in tkn.get().tstack and tkn.get().pri < self.pri:
                right_tree = copy(tkn.get().right)
                self.arg = right_tree
                self.complete = True
                tkn.get().right = self
                result = tkn.get()

            # Если слева операция с большим или таким же приоритетом
            # берем ее как аргумент
            elif 'PBinOperation' in tkn.get().tstack and tkn.get().pri >= self.pri:
                self.arg = tkn.get()
                self.complete = True

            else:
                return None

            exp = PExpression()
            exp.child = result
            return exp

        return None

    def right_reduce(self, tkn):
        if 'PValue' in tkn.tstack:
            self.arg = tkn.get()
            self.complete = True
        else:
            return None

        exp = PExpression()
        exp.child = self
        return exp

    def __str__(self):
        return '{{{}{}}}'.format(
            self.str_value,
            self.arg
        )
