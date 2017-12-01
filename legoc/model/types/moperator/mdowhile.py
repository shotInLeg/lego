from legoc.model.types.moperator.moperator import MOperator


class MDoWhile(MOperator):
    def __init__(self, mexp, lst_instr):
        super(MDoWhile, self).__init__()
        self.tstack.append(MDoWhile.__name__)

        self.cond = mexp
        self.instructions = lst_instr
