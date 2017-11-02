from legoc.parser.types.psequence.pparams import PParams


class PFormalParams(PParams):
    def __init__(self):
        super(PFormalParams, self).__init__()
        self.type_name = 'PFormalParams'

    @staticmethod
    def bb(obr, cbr):
        vctr = PFormalParams()

        return vctr

    @staticmethod
    def bnb(obr, name1, cbr):
        vctr = PFormalParams()
        vctr.lst.append(name1)

        return vctr

    @staticmethod
    def bnlb(obr, name_lst, cbr):
        vctr = PFormalParams()

        for item in name_lst.lst:
            vctr.lst.append(item)

        return vctr

    def __str__(self):
        return '{{{} [{}]}}'.format(
            self.type_name,
            ', '.join([str(x) for x in self.lst])
        )
