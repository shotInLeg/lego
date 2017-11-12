from legoc.parser.types.poperation.poperation import POperation


class PUnOperation(POperation):
    def __init__(self, lexeme):
        super(PUnOperation, self).__init__(lexeme)
        self.tstack.append(PUnOperation.__name__)

        self.arg = None

    def get(self):
        return self
