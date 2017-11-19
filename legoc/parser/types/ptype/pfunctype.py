from legoc.parser.types.ptype.ptype import PType


class PFuncType(PType):
    def __init__(self, ptype=None):
        super(PFuncType, self).__init__()
        self.tstack.append(PFuncType.__name__)

        self.type = ptype
        self.args = []

    def get(self):
        return self

    def __str__(self):
        return '{{Type|{}({})}}'.format(
            self.type,
            ', '.join([str(x) for x in self.args])
        )
