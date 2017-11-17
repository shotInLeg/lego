from legoc.parser.types.pinit.pinit import PInit


class PInitFunc(PInit):
    def __init__(self, modif, lvalue, type, value):
        super(PInitFunc, self).__init__()
        self.tstack.append(PInitFunc.__name__)

        self.modifiers = modif
        self.lvalue = lvalue
        self.return_type = type
        self.value = value

    def get(self):
        return self

    def __str__(self):
        return '{{func\n    [{}]\n    {}\n    {}\n    {}}}'.format(
            ' '.join([str(x) for x in self.modifiers]),
            self.lvalue,
            self.return_type,
            self.value
        )
