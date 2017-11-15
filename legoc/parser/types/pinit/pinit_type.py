from legoc.parser.types.pinit.pinit import PInit


class PInitType(PInit):
    def __init__(self, modif, type_id, type, value):
        super(PInitType, self).__init__()
        self.tstack.append(PInitType.__name__)

        self.modifiers = modif
        self.type_id = type_id
        self.type = type
        self.value = value

    def get(self):
        return self

    def __str__(self):
        return '{{type\n    [{}]\n    {}\n    {}\n    {}}}'.format(
            ' '.join([str(x) for x in self.modifiers]),
            self.type_id,
            self.type,
            self.value
        )
