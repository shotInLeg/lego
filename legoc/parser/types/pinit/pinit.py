from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.pvalue.prvalue import PRValue


class PInit(BaseParserType):
    def __init__(self):
        super(PInit, self).__init__('')
        self.type_name = 'PInit'
        self.complete = True

        self.modif_lst = []
        self.lvalue = None
        self.type = None
        self.value = None

    @classmethod
    def lvalue_o_value(cls, lvalue, _, value):
        if not isinstance(value, PRValue):
            raise ValueError('Требуеться указать тип')

        self = cls()

        self.lvalue = lvalue
        self.type = value.type
        self.value = value

        return self

    @classmethod
    def lvalue_o_type_value(cls, lvalue, _, type1, value):
        self = cls()

        self.lvalue = lvalue
        self.type = type1

        if value.type_name == 'PExpression':
            self.value = value.child
        else:
            self.value = value

        return self

    def __str__(self):
        return '{{{} {} {} {}}}'.format(
            self.type_name,
            self.lvalue,
            self.type,
            self.value
        )
