from legoc.parser.types.base_parser_type import BaseParserType


class PExpression(BaseParserType):
    def __init__(self):
        super(PExpression, self).__init__('')
        self.type_name = 'PExpression'
        self.complete = True

        self.child = None
