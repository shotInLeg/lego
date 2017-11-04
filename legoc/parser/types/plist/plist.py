from legoc.parser.types.base_parser_type import BaseParserType
from legoc.parser.types.psequence.pparams import PParams

class PList(BaseParserType):
    def __init__(self):
        super(PList, self).__init__('')
        self.type_name = 'PList'
        self.complete = True

        self.lst = []

    @classmethod
    def item_o_item(cls, item1, _, item2):
        self = cls()

        if item1.type_name == 'PExpression':
            self.lst.append(item1.child)
        elif isinstance(item1, PParams) and len(item1.lst) == 1:
            self.lst.append(item1.lst[0])
        else:
            self.lst.append(item1)

        if item2.type_name == 'PExpression':
            self.lst.append(item2.child)
        elif isinstance(item2, PParams) and len(item2.lst) == 1:
            self.lst.append(item2.lst[0])
        else:
            self.lst.append(item2)

        return self

    @classmethod
    def list_o_item(cls, lst, _, item):
        self = cls()

        for itm in lst.lst:
            self.lst.append(itm)

        if item.type_name == 'PExpression':
            self.lst.append(item.child)
        elif isinstance(item, PParams) and len(item.lst) == 1:
            self.lst.append(item.lst[0])
        else:
            self.lst.append(item)

        return self

    @classmethod
    def item_o_list(cls, item, _, lst):
        self = cls()

        if item.type_name == 'PExpression':
            self.lst.append(item.child)
        elif isinstance(item, PParams) and len(item.lst) == 1:
            self.lst.append(item.lst[0])
        else:
            self.lst.append(item)

        for itm in lst.lst:
            self.lst.append(itm)

        return self

    def __str__(self):
        return '{{L {}}}'.format(
            ', '.join([str(x) for x in self.lst])
        )
