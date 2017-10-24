from legoc.parser.types.plist.plist import PList


class PDefineList(PList):
    def __init__(self):
        super(PDefineList, self).__init__()
        self.type_name = 'PDefineList'
