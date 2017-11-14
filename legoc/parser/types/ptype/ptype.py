from legoc.parser.types.base_parser_type import BaseParserType


class PType(BaseParserType):
    def __init__(self):
        super(PType, self).__init__()
        self.tstack.append(PType.__name__)

    def get(self):
        return self

    def __str__(self):
        return '{{Type|None}}'
