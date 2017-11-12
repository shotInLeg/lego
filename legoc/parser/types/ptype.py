from legoc.parser.types.base_parser_type import BaseParserType


class PType(BaseParserType):
    def __init__(self, lexeme):
        super(PType, self).__init__()
        self.parents.add(PType.__name__)
        self.str_value = lexeme
        self.type = ''
        self.prms = None

    def get(self):
        return self

    def __str__(self):
        if self.type in ['Function', 'Template']:
            return '({}){}'.format(
                ', '.join([str(x) for x in self.prms]),
                self.str_value
            )
        return '{}'.format(
            self.str_value
        )
