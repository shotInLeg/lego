from legoc.parser.types.pname.pname import PName


class PFuncName(PName):
    def __init__(self, lexem):
        super(PFuncName, self).__init__(lexem)
        self.type_name = 'PFuncName'
