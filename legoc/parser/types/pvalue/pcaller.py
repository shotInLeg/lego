from legoc.parser.types.pvalue.plvalue import PLValue


class PCaller(PLValue):
    def __init__(self):
        super(PLValue, self).__init__('')
        self.type_name = 'PCaller'
        self.complete = True

        self.obj = None
        self.params = []

    @classmethod
    def type_params(cls, type1, params):
        self = cls()

        self.obj = type1

        for prm in params.lst:
            self.params.append(prm)

        return self

    @classmethod
    def value_params(cls, value, params):
        self = cls()

        self.obj = value

        for prm in params.lst:
            self.params.append(prm)

        return self

    def __str__(self):
        return '{{{} {}({})}}'.format(
            self.type_name,
            self.obj,
            ', '.join([str(x) for x in self.params])
        )
