from legoc.parser.types.base_parser_type import BaseParserType


class PList(BaseParserType):
    def __init__(self):
        super(PList, self).__init__('')
        self.type_name = 'PList'
        self.complete = True

        self.lst = []
