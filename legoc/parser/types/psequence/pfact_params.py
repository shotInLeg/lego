from legoc.parser.types.psequence.pparams import PParams


class PFactParams(PParams):
    def __init__(self):
        super(PFactParams, self).__init__()
        self.type_name = 'PFactParams'

    @staticmethod
    def beb(obr, expr, cbr):
        vctr = PFactParams()
        vctr.lst.append(expr.child)
        return vctr

    @staticmethod
    def bvb(obr, val1, cbr):
        vctr = PFactParams()
        vctr.lst.append(val1)

        return vctr

    @staticmethod
    def belb(obr, expr_lst, cbr):
        vctr = PFactParams()

        for item in expr_lst.lst:
            vctr.lst.append(item)

        return vctr

    def __str__(self):
        return '{{{} [{}]}}'.format(
            self.type_name,
            ', '.join([str(x) for x in self.lst])
        )
