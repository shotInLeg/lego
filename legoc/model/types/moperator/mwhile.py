from legoc.model.types.moperator.moperator import MOperator


class MWhile(MOperator):
    def __init__(self, mexp, lst_instr):
        super(MWhile, self).__init__()
        self.tstack.append(MWhile.__name__)

        self.cond = mexp
        self.instructions = lst_instr
