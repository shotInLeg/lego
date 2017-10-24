from legoc.parser.types.poperation.pimmutable_operation import (
    PImmutableOperation
)


class PLogicOperation(PImmutableOperation):
    def __init__(self, lexem, priority=0):
        super(PLogicOperation, self).__init__(lexem, priority)
        self.type_name = 'PLogicOperation'
