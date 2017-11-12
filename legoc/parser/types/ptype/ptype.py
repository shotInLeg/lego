from legoc.parser.types.base_parser_type import BaseParserType


class PType(BaseParserType):
    def __init__(self, lexeme):
        super(PType, self).__init__()
        self.tstack.append(PType.__name__)
        self.str_value = lexeme

    def get(self):
        return self
