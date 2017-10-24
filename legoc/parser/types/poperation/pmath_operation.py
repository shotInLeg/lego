from legoc.parser.types.poperation.pimmutable_operation import (
    PImmutableOperation
)


class PMathOperation(PImmutableOperation):
    def __init__(self, lexem, priority=0):
        super(PMathOperation, self).__init__(lexem, priority)
        self.type_name = 'PMathOperation'
