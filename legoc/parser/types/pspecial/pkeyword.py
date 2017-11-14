from legoc.parser.types.base_parser_type import BaseParserType


class PKeyword(BaseParserType):
    def __init__(self, lexeme):
        super(PKeyword, self).__init__()
        self.tstack.append(PKeyword.__name__)
        self.str_value = lexeme

    def get(self):
        return self
