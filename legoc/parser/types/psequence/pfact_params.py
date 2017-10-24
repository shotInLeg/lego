from legoc.parser.types.base_parser_type import BaseParserType


class PFactParamList(BaseParserType):
    def __init__(self):
        super(PFactParamList, self).__init__('')
        self.type_name = 'PFactParamList'
