from legoc.parser.types.pvalue.prvalue import PRValue


class PExpression(PRValue):
    def __init__(self):
        super(PExpression, self).__init__('')
        self.type_name = 'PExpression'
        self.complete = True

        self.child = None

    @staticmethod
    def vov(val1, oper, val2):
        exp = PExpression()

        if val1.type_name == 'PExpression':
            oper.left_arg = val1.child
        else:
            oper.left_arg = val1

        if val2.type_name == 'PExpression':
            oper.right_arg = val2.child
        else:
            oper.right_arg = val2

        exp.child = oper
        return exp

    def __str__(self):
        return '{{{} {}}}'.format(self.type_name, self.child)
