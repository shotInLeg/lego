from legoc.parser.types.base_parser_type import BaseParserType


class PModifier(BaseParserType):
    def __init__(self, lexeme):
        super(PModifier, self).__init__()
        self.tstack.append(PModifier.__name__)
        self.str_value = lexeme

    def get(self):
        return self

    def __str__(self):
        return '{{{}}}'.format(
            self.str_value
        )
