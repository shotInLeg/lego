from legoc.parser.types.base_parser_type import BaseParserType


class POperator(BaseParserType):
    def __init__(self, lexem):
        super(POperator, self).__init__(lexem)
        self.type_name = 'POperator'
        self.complete = True
