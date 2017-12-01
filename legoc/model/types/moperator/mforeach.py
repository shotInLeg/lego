from legoc.model.types.moperator.moperator import MOperator


class MForEach(MOperator):
    def __init__(self, mexp, lst_instr):
        super(MForEach, self).__init__()
        self.tstack.append(MForEach.__name__)

        self.cond = mexp
        self.instructions = lst_instr
