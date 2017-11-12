from legoc.parser.types.base_parser_type import BaseParserType


class POperator(BaseParserType):
    def __init__(self, lexeme):
        super(POperator, self).__init__()
        self.parents.add(POperator.__name__)
        self.str_value = lexeme



    def get(self):
        return self

    def __str__(self):
        return 'Value {}'.format(
            self.str_value
        )
