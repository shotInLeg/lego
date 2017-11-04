from legoc.parser.types.psequence.pparams import PParams


class PFactParams(PParams):
    def __init__(self):
        super(PFactParams, self).__init__()
        self.type_name = 'PFactParams'

    @classmethod
    def b_item_b(cls, ob, item, cb):
        self = cls()

        if item.type_name == 'PExpression':
            self.lst.append(item.child)
        elif isinstance(item, PParams) and len(item.lst) == 1:
            self.lst.append(item.lst[0])
        else:
            self.lst.append(item)

        return self
