from legoc.parser.types.pboperation import PBOperation
from legoc.parser.types.pexpression import PExpression


class PInit(PBOperation):
    def __init__(self, lexeme):
        super(PInit, self).__init__(lexeme)
        self.parents.add(PInit.__name__)
        self.pri = 1
        self.complete = False

        self.modifiers = []
        self.left = None
        self.type = None
        self.right = None

    def get(self):
        return self

    def left_reduce(self, tkn):
        # Добавление левого поддерева
        if 'PValue' in tkn.parents:
            self.left = tkn.get()

        return self

    def right_reduce(self, tkn):

        # Добавление правого поддерева
        if 'PCBrackets' in tkn.parents:
            print('Right: {}'.format(tkn))
            if isinstance(tkn.child, list):
                return None
            elif 'PType' in tkn.get().parents:
                return None

        if 'PType' in tkn.get().parents:
            self.type = tkn.get()

        if 'PValue' in tkn.parents:
            self.right = tkn.get()
            self.complete = True

        if 'PFBrackets' in tkn.parents:
            self.right = tkn.get()
            self.complete = True

        # Возвращение операции как выражения
        if self.complete:
            exp = PExpression()
            exp.child = self
            return exp
        else:
            return self

    def __str__(self):
        return '{{Init [{}] {} {} {} {}}}'.format(
            ', '.join([str(x) for x in self.modifiers]),
            self.left,
            self.str_value,
            self.type,
            self.right
        )
