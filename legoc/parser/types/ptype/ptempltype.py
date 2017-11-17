from legoc.parser.types.ptype.ptype import PType


class PTemplType(PType):
    def __init__(self, ptype=None, args=None):
        super(PTemplType, self).__init__()
        self.tstack.append(PTemplType.__name__)

        self.type = ptype
        self.args = [] if args is None else args

    def get(self):
        return self

    def __str__(self):
        return '{{Type|{}<{}>}}'.format(
            self.type,
            ', '.join([str(x) for x in self.args])
        )
