from legoc.parser.types.pvalue.prvalue import PRValue


class PObject(PRValue):
    def __init__(self):
        super(PObject, self).__init__('')
        self.type_name = 'PObject'
        self.complete = True
