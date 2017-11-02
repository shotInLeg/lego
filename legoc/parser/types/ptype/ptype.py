from legoc.parser.types.base_parser_type import BaseParserType


class PType(BaseParserType):
    def __init__(self, lexem):
        super(PType, self).__init__(lexem)
        self.type_name = 'PType'
        self.complete = True
