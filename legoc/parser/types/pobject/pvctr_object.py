from legoc.parser.types.pobject.pobject import PObject


class PVctrObject(PObject):
    def __init__(self):
        super(PVctrObject, self).__init__()
        self.type_name = 'PVctrObject'
        self.complete = True
