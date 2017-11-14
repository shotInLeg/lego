from legoc.parser.types.ptype.ptype import PType


class PSimpleType(PType):
    def __init__(self, lexeme):
        super(PSimpleType, self).__init__()
        self.tstack.append(PSimpleType.__name__)
        self.str_value = lexeme

    def get(self):
        return self

    def __str__(self):
        return '{{Type|{}}}'.format(
            self.str_value
        )
