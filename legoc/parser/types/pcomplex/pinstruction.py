from legoc.parser.types.base_parser_type import BaseParserType


class PInstruction(BaseParserType):
    def __init__(self):
        super(PInstruction, self).__init__('')
        self.type_name = 'PInstruction'
        self.complete = True

        self.child = None

    @staticmethod
    def bo(some, opr):
        inst = PInstruction()
        if some.type_name == 'PExpression':
            inst.child = some.child
        else:
            inst.child = some

        return inst

    def __str__(self):
        return '{{{} {}}}'.format(self.type_name, self.child)
