from legoc.parser.types.base_parser_type import BaseParserType


class POperator(BaseParserType):
    def __init__(self, lexeme):
        super(POperator, self).__init__()
        self.tstack.append(POperator.__name__)
        self.complete = False
        self.str_value = lexeme

    def get(self):
        return self
