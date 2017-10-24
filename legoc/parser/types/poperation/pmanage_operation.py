from legoc.parser.types.poperation.pimmutable_operation import (
    PImmutableOperation
)


class PManageOperation(PImmutableOperation):
    def __init__(self, lexem, priority=0):
        super(PManageOperation, self).__init__(lexem, priority)
        self.type_name = 'PManageOperation'
