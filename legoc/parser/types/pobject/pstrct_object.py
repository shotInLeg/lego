from legoc.parser.types.pobject.pobject import PObject


class PStrctObject(PObject):
    def __init__(self):
        super(PStrctObject, self).__init__()
        self.type_name = 'PStrctObject'
        self.complete = True
