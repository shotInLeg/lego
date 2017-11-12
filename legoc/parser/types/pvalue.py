from legoc.parser.types.base_parser_type import BaseParserType


class PValue(BaseParserType):
    def __init__(self, lexeme):
        super(PValue, self).__init__()
        self.parents.add(PValue.__name__)
        self.str_value = lexeme

    def get(self):
        return self

    def __str__(self):
        return 'Value {}'.format(
            self.str_value
        )
