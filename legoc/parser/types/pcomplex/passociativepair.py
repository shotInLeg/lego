from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.psequence.pparams import PParams
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

    @classmethod
    def item_o_item(cls, item1, _, item2):
        self = cls()

        # Init Key
        if isinstance(item1, PParams) and len(item1.lst) == 1:
            self.key = item1.lst[0]
            if isinstance(item1.lst[0], PRValue):
                self.key_type = item1.lst[0].type
        else:
            self.key = item1
            if isinstance(item1, PRValue):
                self.key_type = item1.type

        # Init Value
        if isinstance(item2, PParams) and len(item2.lst) == 1:
            self.value = item2.lst[0]
            if isinstance(item2.lst[0], PRValue):
                self.value_type = item2.lst[0].type
        else:
            self.value = item2
            if isinstance(item2, PRValue):
                self.value_type = item2.type

        return self

    @classmethod
    def item_o_type_item(cls, item1, _, type1, item2):
        self = cls()

        # Init Key
        if isinstance(item1, PParams) and len(item1.lst) == 1:
            self.key = item1.lst[0]
            if isinstance(item1.lst[0], PRValue):
                self.key_type = item1.lst[0].type
        else:
            self.key = item1
            if isinstance(item1, PRValue):
                self.key_type = item1.type

        # Init Value
        self.value_type = type1
        self.value = item2

        return self

    def __str__(self):
        return '{{{} {} {}:{}}}'.format(
            self.type_name,
            self.type,
            self.key,
            self.value
        )
