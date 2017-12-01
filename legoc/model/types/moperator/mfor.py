from legoc.model.types.moperator.moperator import MOperator


class MFor(MOperator):
    def __init__(self, lst_def, mexp, lst_mexp, lst_instr):
        super(MFor, self).__init__()
        self.tstack.append(MFor.__name__)

        self.starts = lst_def
        self.cond = mexp
        self.steps = lst_mexp
        self.instructions = lst_instr
