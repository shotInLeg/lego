from legoc.parser.types.poperation.poperation import POperation


class PMutableOperation(POperation):
    def __init__(self, lexem, priority=0):
        super(PMutableOperation, self).__init__(lexem, priority)
        self.type_name = 'PMutableOperation'
