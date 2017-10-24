from legoc.parser.types.base_parser_type import BaseParserType


class POperationType(BaseParserType):
    def __init__(self, lexem):
        super(POperationType, self).__init__(lexem)
        self.type_name = 'POperationType'
        self.la = True
        self.ra = True

        self.left_arg = None
        self.right_arg = None

    def left_reduce(self, token):
        if token.type_name == 'PNameType':
            self.left_arg = token
            return self

        return None

    def right_reduce(self, token):
        if token.type_name == 'PNameType':
            self.right_arg = token
            return self

        return None
