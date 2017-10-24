from legoc.parser.types.plist.plist import PList


class PValueList(PList):
    def __init__(self):
        super(PValueList, self).__init__()
        self.type_name = 'PValueList'
