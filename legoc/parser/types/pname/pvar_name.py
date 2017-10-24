from legoc.parser.types.pname.pname import PName


class PVarName(PName):
    def __init__(self, lexem):
        super(PVarName, self).__init__(lexem)
        self.type_name = 'PVarName'
