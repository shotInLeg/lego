from legoc.model.types.moperator.moperator import MOperator


class MWith(MOperator):
    def __init__(self, lst_def, lst_instr):
        super(MWith, self).__init__()
        self.tstack.append(MWith.__name__)

        self.defines = lst_def
        self.instructions = lst_instr
