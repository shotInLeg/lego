from legoc.parser.types.pvalue.plvalue import PLValue


class PType(PLValue):
    def __init__(self):
        super(PType, self).__init__()
        self.tstack.append(PType.__name__)

    def get(self):
        return self

    def __str__(self):
        return '{{Type|None}}'
