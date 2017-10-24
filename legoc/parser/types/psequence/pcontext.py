from legoc.parser.types.base_parser_type import BaseParserType


class PContextObject(BaseParserType):
    def __init__(self):
        super(PContextObject, self).__init__('')
        self.type_name = 'PContext'

        self.lst = []

    def __str__(self):
        return '{{CNT {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
