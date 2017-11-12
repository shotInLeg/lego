from legoc.parser.types.pvalue.plvalue import PLValue


class PName(PLValue):
    def __init__(self, lexeme):
        super(PName, self).__init__()
        self.tstack.append(PName.__name__)
        self.str_value = lexeme
