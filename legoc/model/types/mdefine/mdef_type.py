from legoc.model.types.mdefine.mdef import MDef


class MDefType(MDef):
    def __init__(self, modifiers, name, lst_templ_names, lst_parent_names, lst_def):
        super(MDefFunc, self).__init__()
        self.tstack.append(MDefFunc.__name__)

        self.modifiers = modifiers
        self.name = name
        self.templates = lst_templ_names
        self.parents = lst_parent_names
        self.defines = lst_def
