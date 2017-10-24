from legoc.parser.types.pvalue.plvalue import PLValue


class PObject(PLValue):
    def __init__(self):
        super(PObject, self).__init__('')
        self.type_name = 'PObject'
        self.complete = True
