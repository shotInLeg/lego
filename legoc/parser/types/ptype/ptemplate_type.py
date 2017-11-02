from legoc.parser.types.ptype.pcomplex_type import PComplexType


class PTemplateType(PComplexType):
    def __init__(self, lexem):
        super(PTemplateType, self).__init__(lexem)
        self.type_name = 'PTemplateType'

        self.tmpl_args = []

    def add_template_arg(self, ptype):
        self.tmpl_args.append(ptype)

    def __str__(self):
        return '{{{} {}<{}>}}'.format(
            self.type_name,
            self.str_value,
            ','.join([str(x) for x in self.tmpl_args])
        )