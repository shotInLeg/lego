from legoc.parser.types.poperation.poperation import POperation


class PBinOperation(POperation):
    def __init__(self, lexeme):
        super(PBinOperation, self).__init__(lexeme)
        self.tstack.append(PBinOperation.__name__)

        self.pri = self.priority[lexeme]
        self.left = None
        self.right = None

    def get(self):
        return self
