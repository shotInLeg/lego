from legoc.parser.types.base_parser_type import BaseParserType


class PKeyword(BaseParserType):
    def __init__(self, lexem):
        super(PKeyword, self).__init__(lexem)
        self.type_name = 'PKeyword'
        self.complete = True
