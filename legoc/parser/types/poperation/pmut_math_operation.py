from legoc.parser.types.poperation.pmutable_operation import (
    PMutableOperation
)


class PMutMathOperation(PMutableOperation):
    def __init__(self, lexem, priority=0):
        super(PMutableOperation, self).__init__(lexem, priority)
        self.type_name = 'PMutableOperation'
