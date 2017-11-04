from legoc.parser.types.poperation.pimmutable_operation import (
    PImmutableOperation
)
from legoc.parser.types.pvalue.prvalue import PRValue


class PUnaryOperation(PImmutableOperation, PRValue):
    def __init__(self, lexem, priority=0):
        super(PUnaryOperation, self).__init__(lexem, priority)
        self.type_name = 'PUnaryOperation'

    @classmethod
    def b_operation_item_b(cls, ob, oper, item, cb):
        self = cls()

        self.left_arg = None
        self.str_value = oper.str_value
        self.right_arg = item

        return self
