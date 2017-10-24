from legoc.parser.types.base_parser_type import BaseParserType


class PValue(BaseParserType):
    def __init__(self, lexem):
        super(PValue, self).__init__(lexem)
        self.type_name = 'PValue'
        self.complete = True
