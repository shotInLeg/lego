from legoc.parser.types.plist.plist import PList


class PInstructionList(PList):
    def __init__(self):
        super(PInstructionList, self).__init__()
        self.type_name = 'PInstructionList'

    def __str__(self):
        return '{{LI {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
