from legoc.parser.types.base_parser_type import BaseParserType


class POperation(BaseParserType):
    def __init__(self, lexem, priority=0):
        super(POperation, self).__init__(lexem)
        self.type_name = 'POperation'

        self.priority = priority
        self.left_arg = None
        self.right_arg = None

    def __str__(self):
        if self.complete:
            view = '{{{} {} {} {}}}'.format(
                self.type_name, self.left_arg,
                self.str_value, self.right_arg
            )
        else:
            view = '{{{} {} {} {} {}}}'.format(
                self.type_name, self.left_arg,
                self.str_value, self.right_arg,
                self.complete
            )

        return view
