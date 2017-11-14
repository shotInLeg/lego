from legoc.parser.types.pinit.pinit import PInit


class PInitValue(PInit):
    def __init__(self, modif, lvalue, type, value):
        super(PInitValue, self).__init__()
        self.tstack.append(PInitValue.__name__)

        self.modifiers = modif
        self.lvalue = lvalue
        self.type = type
        self.value = value

    def get(self):
        return self

    def __str__(self):
        return '{{init\n    [{}]\n    {}\n    {}\n    {}}}'.format(
            ' '.join([str(x) for x in self.modifiers]),
            self.lvalue,
            self.type,
            self.value
        )
