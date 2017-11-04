from legoc.parser.types.pinit.pinit import PInit


class PInitVar(PInit):
    def __init__(self):
        super(PInitVar, self).__init__()
        self.type_name = 'PDefineVar'
        self.complete = True
