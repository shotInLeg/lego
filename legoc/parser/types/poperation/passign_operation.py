from legoc.parser.types.poperation.poperation import POperation


class PAssignOperation(POperation):
    def __init__(self, lexem, priority=0):
        super(PAssignOperation, self).__init__(lexem, priority)
        self.type_name = 'PAssignOperation'
