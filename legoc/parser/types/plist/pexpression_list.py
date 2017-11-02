from legoc.parser.types.plist.pvalue_list import PValueList


class PExpressionList(PValueList):
    def __init__(self):
        super(PExpressionList, self).__init__()
        self.type_name = 'PExpressionList'

    @staticmethod
    def vov(val1, oper, val2):
        self = PExpressionList()

        if val1.type_name == 'PExpression':
            self.lst.append(val1.child)
        else:
            self.lst.append(val1)

        if val2.type_name == 'PExpression':
            self.lst.append(val2.child)
        else:
            self.lst.append(val2)

        return self

    @staticmethod
    def eov(expr_list, oper, val2):
        self = PExpressionList()
        for item in expr_list.lst:
            self.lst.append(item)
        self.lst.append(val2)
        return self

    @staticmethod
    def voe(val1, oper, expr_list):
        self = PExpressionList()
        self.lst.append(val1)
        for item in expr_list.lst:
            self.lst.append(item)
        return self

    def __str__(self):
        return '{{LE {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
