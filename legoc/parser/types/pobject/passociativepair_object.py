from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.pvalue.prvalue import PRValue
from legoc.parser.types.ptype.psimple_type import PSimpleType


class PAssociativePair(BaseParserType):
    def __init__(self):
        super(PAssociativePair, self).__init__('')
        self.type_name = 'PAssociativePair'
        self.complete = True

        self.type = PSimpleType('AssociativePair')
        self.key = None
        self.key_type = PSimpleType('Any')
        self.value = None
        self.value_type = PSimpleType('Any')

    @staticmethod
    def vov(val1, oper, val2):
        pair = PAssociativePair()

        pair.key = val1
        if isinstance(val1, PRValue):
            pair.key_type = val1.type

        pair.value = val2
        if isinstance(val2, PRValue):
            pair.value_type = val2.type

        return pair

    def __str__(self):
        return '{{{} {} {}:{}}}'.format(
            self.type_name,
            self.type,
            self.key,
            self.value
        )
