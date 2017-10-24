from legoc.parser.types.pobject.pobject import PObject


class PDictObject(PObject):
    def __init__(self):
        super(PDictObject, self).__init__()
        self.type_name = 'PDictObject'
        self.complete = True
