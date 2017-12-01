from legoc.model.types.mdefine.mdef import MDef


class MDefFunc(MDef):
    def __init__(self, modifiers, name, lst_arg_names, lst_arg_types, return_type, lst_instr):
        super(MDefFunc, self).__init__()
        self.tstack.append(MDefFunc.__name__)

        self.modifiers = modifiers
        self.name = name
        self.arg_names = lst_arg_names
        self.arg_types = lst_arg_types
        self.return_type = return_type
        self.instructions = lst_instr
