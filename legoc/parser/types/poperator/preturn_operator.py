from legoc.parser.types.poperator.poperator import POperator


class PReturnOperator(POperator):
    def __init__(self):
        super(PReturnOperator, self).__init__('return')
        self.type_name = 'PReturnOperator'
        self.complete = True

        self.value = None


    @classmethod
    def o_item(cls, _, item):
        self = cls()

        if item.type_name == 'PExpresson':
            self.value = item.child
        elif item.type_name == 'PInstruction':
            self.value = item.child
        else:
            self.value = item

        return self

    def __str__(self):
        return '{{{} {}}}'.format(
            self.type_name,
            self.value
        )
