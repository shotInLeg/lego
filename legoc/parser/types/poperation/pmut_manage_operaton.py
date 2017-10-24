from legoc.parser.types.poperation.pmutable_operation import (
    PMutableOperation
)


class PMutManageOperation(PMutableOperation):
    def __init__(self, lexem, priority=0):
        super(PMutManageOperation, self).__init__(lexem, priority)
        self.type_name = 'PMutManageOperation'
