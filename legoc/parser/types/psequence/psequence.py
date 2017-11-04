from legoc.parser.types.base_parser_type import BaseParserType


class PSequence(BaseParserType):
    def __init__(self):
        super(PSequence, self).__init__('')
        self.type_name = 'PSequence'
        self.complete = True

        self.lst = []

    @classmethod
    def b_b(cls, *_):
        self = cls()
        return self

    @classmethod
    def b_item_b(cls, ob, item, cb):
        self = cls()

        if item.type_name == 'PExpression':
            self.lst.append(item.child)
        elif item.type_name == 'PInstruction':
            self.lst.append(item.child)
        else:
            self.lst.append(item)

        return self

    @classmethod
    def b_itemlist_b(cls, ob, item_list, cb):
        self = cls()

        for item in item_list.lst:
            self.lst.append(item)

        return self

    def __str__(self):
        return '{{{} [{}]}}'.format(
            self.type_name,
            ', '.join([str(x) for x in self.lst])
        )
