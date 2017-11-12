from copy import copy

from legoc.parser.types.error_string import UNARY_NEED_BRACKTES, NEED_PARAMS
from legoc.parser.types.settings import (
    priority, bin_oper_lst, un_dpl_oper_lst, bracket_oper_lst
)
from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.pexpression import PExpression
from legoc.parser.types.puoperation import PUOperation


class PBOperation(BaseParserType):
    def __init__(self, lexeme):
        super(PBOperation, self).__init__()
        self.parents.add(PBOperation.__name__)
        self.str_value = lexeme
        self.pri = priority[lexeme]
        self.complete = False

        self.left = None
        self.right = None
        self.brackets = False

    def get(self):
        return self

    def left_reduce(self, tkn):
        # Добавление левого поддерева
        if 'PValue' in tkn.parents:
            if 'PCBrackets' in tkn.parents and \
                    'PBOperation' in tkn.get().parents:
                tkn.get().brackets = True
            self.left = tkn.get()

        # Преобразование из унарной в бинарную
        elif self.str_value in un_dpl_oper_lst:
            raise ValueError('{} -: {}'.format(
                tkn, UNARY_NEED_BRACKTES
            ))

        else:
            return None

        return self

    def right_reduce(self, tkn):

        res = None
        # Унарной операции -
        if self.left is None and self.str_value in un_dpl_oper_lst:
            res = self.update_unary(tkn)
            exp = PExpression()
            exp.child = res
            return exp

        # Обработка операций-скобок (), []
        if self.str_value in bracket_oper_lst:
            res = self.update_brackets(tkn)

        # Обработка обычный бинарных операций
        if self.str_value in bin_oper_lst:
            res = self.update_binary(tkn)

        if res is None:
            return None

        exp = PExpression()
        exp.child = self.restore_priority(res)
        return exp

    def update_unary(self, tkn):
        unar = PUOperation(self.str_value)
        unar.arg = tkn.get()
        unar.complete = True
        return unar

    def update_brackets(self, tkn):
        if 'PCBrackets' in tkn.parents:
            self.right = tkn.child if isinstance(tkn.child, list) \
                else [tkn.child]
            self.complete = True
        else:
            raise ValueError('Ожидался список параметров')

        return self

    def update_binary(self, tkn):
        if 'PValue' in tkn.parents:
            if 'PCBrackets' in tkn.parents and \
                    'PBOperation' in tkn.get().parents:
                tkn.get().brackets = True
            self.right = tkn.get()
            self.complete = True
            return self
        return None

    def restore_priority(self, boperation):
        top_tree = copy(boperation)
        left_tree = copy(boperation.left)

        result = top_tree
        if 'PBOperation' in left_tree.parents:
            if left_tree.pri < top_tree.pri and not left_tree.brackets:
                left_tree_right = copy(left_tree.right)
                top_tree.left = left_tree_right
                left_tree.right = top_tree
                result = left_tree

        return result

    def __str__(self):
        if self.str_value == '()':
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
