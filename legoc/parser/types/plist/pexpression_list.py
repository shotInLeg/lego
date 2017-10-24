from legoc.parser.types.plist.pvalue_list import PValueList


class PExpressionList(PValueList):
    def __init__(self):
        super(PExpressionList, self).__init__()
        self.type_name = 'PExpressionList'

    @staticmethod
    def von(val1, oper, name1):
        self = PExpressionList()

        self.lst.append(val1)
        self.lst.append(name1)

        return self

    @staticmethod
    def nov(name1, oper, val1):
        self = PExpressionList()

        self.lst.append(name1)
        self.lst.append(val1)

        return self

    @staticmethod
    def eov(expr, oper, val1):
        self = PExpressionList()

        self.lst.append(expr.child)
        self.lst.append(val1)

        return self

    @staticmethod
    def eon(expr, oper, name1):
        self = PExpressionList()

        self.lst.append(expr.child)
        self.lst.append(name1)

        return self

    @staticmethod
    def voe(val1, oper, expr):
        self = PExpressionList()

        self.lst.append(val1)
        self.lst.append(expr.child)

        return self

    @staticmethod
    def noe(name1, oper, expr):
        self = PExpressionList()

        self.lst.append(name1)
        self.lst.append(expr.child)

        return self

    @staticmethod
    def eol(expr, oper, list1):
        self = PExpressionList()

        self.lst.append(expr.child)
        self.lst.extend(list1.lst)

        return self

    @staticmethod
    def loe(list1, oper, expr):
        self = PExpressionList()

        self.lst.extend(list1.lst)
        self.lst.append(expr.child)

        return self

    @staticmethod
    def nlov(nlist1, oper, val1):
        self = PExpressionList()

        self.lst.extend(nlist1.lst)
        self.lst.append(val1)

        return self

    @staticmethod
    def elov(elist1, oper, val1):
        elist1.lst.append(val1)
        return elist1

    @staticmethod
    def elon(elist1, oper, name1):
        elist1.lst.append(name1)
        return elist1

    @staticmethod
    def voel(val1, oper, elist1):
        self = PExpressionList()

        self.lst.append(val1)
        self.lst.extend(elist1.lst)

        return self

    @staticmethod
    def noel(name1, oper, elist1):
        self = PExpressionList()

        self.lst.append(name1)
        self.lst.extend(elist1.lst)

        return self

    def __str__(self):
        return '{{LE {}}}'.format(
            ', '.join(
                [str(x) for x in self.lst]
            )
        )
