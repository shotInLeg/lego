from legoc.parser.types.base_parser_type import BaseParserType


class PValue(BaseParserType):
    def __init__(self):
        super(PValue, self).__init__()
        self.tstack.append(PValue.__name__)

    def get(self):
        return self
