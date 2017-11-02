from legoc.parser.types.base_parser_type import BaseParserType


class PDefine(BaseParserType):
    def __init__(self):
        super(PDefine, self).__init__('')
        self.type_name = 'PDefine'
        self.complete = True

        self.name = None
        self.type = None
        self.value = None

    def __str__(self):
        return '{{{} {} {} {}}}'.format(
            self.type_name,
            self.name,
            self.type,
            self.value
        )
