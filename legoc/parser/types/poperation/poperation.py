from legoc.parser.types.base_parser_type import BaseParserType


class POperation(BaseParserType):
    un = [
        '!'
    ]

    bin = [

    ]

    un_and_bin = [
        '-'
    ]

    priority = {

    }

    def __init__(self, lexeme):
        super(POperation, self).__init__()
        self.tstack.append(POperation.__name__)
        self.complete = False
        self.str_value = lexeme

    def get(self):
        return self
