from legoc.parser.types.base_parser_type import BaseParserType


class PSequence(BaseParserType):
    def __init__(self):
        super(PSequence, self).__init__('')
        self.type_name = 'PSequence'
        self.complete = True

        self.lst = []
