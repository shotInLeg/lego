from legoc.parser.types.base_parser_type import BaseParserType


class PInit(BaseParserType):
    def __init__(self):
        super(PInit, self).__init__()
        self.tstack.append(PInit.__name__)

    def get(self):
        return self
