from legoc.parser.types.base_parser_type import BaseParserType


class PFBrackets(BaseParserType):
    def __init__(self, child=None):
        super(PFBrackets, self).__init__()
        self.tstack.append(PFBrackets.__name__)
        self.child = child

    def get(self):
        return self.child
