from legoc.parser.types.poperation.poperation import POperation


class PImmutableOperation(POperation):
    def __init__(self, lexem, priority=0):
        super(PImmutableOperation, self).__init__(lexem, priority)
        self.type_name = 'PImmutableOperation'
