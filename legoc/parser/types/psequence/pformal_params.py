from legoc.parser.types.base_parser_type import BaseParserType


class PFormalParamList(BaseParserType):
    def __init__(self):
        super(PFormalParamList, self).__init__('')
        self.type_name = 'PFormalParamList'
