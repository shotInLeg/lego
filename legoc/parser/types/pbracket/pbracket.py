from legoc.parser.types.base_parser_type import BaseParserType


class PBracket(BaseParserType):
    def __init__(self, lexem, num):
        super(PBracket, self).__init__(lexem)
        self.type_name = 'PBracket'
        self.complete = True
        self.num = num
