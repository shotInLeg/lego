from legoc.parser.types.ptype.pcomplex_type import PComplexType


class PTemplateType(PComplexType):
    def __init__(self):
        super(PTemplateType, self).__init__()
        self.type_name = 'PTemplateType'
