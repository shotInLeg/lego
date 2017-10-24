from legoc.parser.types.poperation.pmutable_operation import (
    PMutableOperation
)


class PMutLogicOperation(PMutableOperation):
    def __init__(self, lexem, priority=0):
        super(PMutLogicOperation, self).__init__(lexem, priority)
        self.type_name = 'PMutLogicOperation'
