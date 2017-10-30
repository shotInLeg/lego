from legoc.parser.types.base_parser_type import BaseParserType


class PInstruction(BaseParserType):
    def __init__(self):
        super(PInstruction, self).__init__('')
        self.type_name = 'PInstruction'
        self.complete = True

        self.child = None
