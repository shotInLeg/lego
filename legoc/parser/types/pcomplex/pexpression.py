from legoc.parser.types.pvalue.plvalue import PLValue
from legoc.parser.types.psequence.pparams import PParams


class PExpression(PLValue):
    def __init__(self):
        super(PExpression, self).__init__('')
        self.type_name = 'PExpression'
        self.complete = True

        self.child = None

    @classmethod
    def item_operation_item(cls, item1, oper, item2):
        self = cls()

        if item1.type_name == 'PExpression':
            oper.left_arg = item1.child
        elif isinstance(item1, PParams) and len(item1.lst) == 1:
            oper.left_arg = item1.lst[0]
        else:
            oper.left_arg = item1

        if item2.type_name == 'PExpression':
            oper.right_arg = item2.child
        elif isinstance(item2, PParams) and len(item2.lst) == 1:
            oper.right_arg = item2.lst[0]
        else:
            oper.right_arg = item2

        self.child = oper
        return self

    def __str__(self):
        return '{{{} {}}}'.format(self.type_name, self.child)
