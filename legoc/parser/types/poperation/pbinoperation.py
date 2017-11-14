from copy import copy

from legoc.parser.types.poperation.poperation import POperation
from legoc.parser.types.poperation.punoperation import PUnOperation
from legoc.parser.types.pexp.pexpression import PExpression


class PBinOperation(POperation):
    def __init__(self, lexeme):
        super(PBinOperation, self).__init__(lexeme)
        self.tstack.append(PBinOperation.__name__)

        self.pri = self.priority[lexeme]
        self.left = None
        self.right = None
        self.brackets = False

    def get(self):
        return self

    def left_reduce(self, tkn):
        # Добавление левого поддерева
        if 'PValue' in tkn.tstack:
            if 'PCBrackets' in tkn.tstack and \
                    'PBinOperation' in tkn.get().tstack:
                tkn.get().brackets = True
            self.left = tkn.get()

        # Преобразование из унарной в бинарную
        elif self.str_value in self.un_and_bin:
            raise ValueError('{} -: {}'.format(
                tkn, 'Необходимо заключить в скобки'
            ))

        else:
            return None

        return self

    def right_reduce(self, tkn):

        res = None
        # Унарной операции -
        if self.left is None and self.str_value in self.un_and_bin:
            res = self.update_unary(tkn)
            exp = PExpression()
            exp.child = res
            return exp

        # Обработка операций-скобок (), []
        if self.str_value in self.brac:
            res = self.update_brackets(tkn)

        # Обработка обычный бинарных операций
        if self.str_value in self.bin:
            res = self.update_binary(tkn)

        if res is None:
            return None

        exp = PExpression()
        exp.child = self.restore_priority(res)
        return exp

    def update_unary(self, tkn):
        unar = PUnOperation(self.str_value)
        unar.arg = tkn.get()
        unar.complete = True
        return unar

    def update_brackets(self, tkn):
        if 'PCBrackets' in tkn.tstack:
            self.right = tkn.get_list()
            self.complete = True
        else:
            raise ValueError('Ожидался список параметров')

        return self

    def update_binary(self, tkn):
        if 'PValue' in tkn.tstack:
            if 'PCBrackets' in tkn.tstack and \
                    'PBinOperation' in tkn.get().tstack:
                tkn.get().brackets = True
            self.right = tkn.get()
            self.complete = True
            return self
        return None

    def restore_priority(self, boperation):
        top_tree = copy(boperation)
        left_tree = copy(boperation.left)

        result = top_tree
        if 'PBinOperation' in left_tree.tstack:
            if left_tree.pri < top_tree.pri and not left_tree.brackets:
                left_tree_right = copy(left_tree.right)
                top_tree.left = left_tree_right
                left_tree.right = top_tree
                result = left_tree

        return result

    def __str__(self):
        if self.str_value in self.brac:
            return '{{{} {} [{}]}}'.format(
                self.left,
                self.str_value,
                ', '.join([str(x) for x in self.right])
            )

        return '{{{} {} {}}}'.format(
            self.left,
            self.str_value,
            self.right
        )
