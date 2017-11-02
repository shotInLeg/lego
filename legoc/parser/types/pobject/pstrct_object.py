from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.ptype.psimple_type import PSimpleType


class PStrctObject(BaseParserType):
    def __init__(self):
        super(PStrctObject, self).__init__('')
        self.type_name = 'PStrctObject'
        self.complete = True

        self.type = PSimpleType('Strct')
        self.lst = []

    @staticmethod
    def bab(obr, asgn, cbr):
        vctr = PStrctObject()

        return vctr

    @staticmethod
    def bdb(obr, def1, cbr):
        vctr = PStrctObject()
        vctr.lst.append(def1)

        return vctr

    @staticmethod
    def bdlb(obr, def_lst, cbr):
        vctr = PStrctObject()

        for item in def_lst.lst:
            vctr.lst.append(item)

        return vctr

    def __str__(self):
        return '{{{} {} [{}]}}'.format(
            self.type_name,
            self.type,
            ', '.join([str(x) for x in self.lst])
        )
