from legoc.parser.types.pobject.pcontainer import PContainer
from legoc.parser.types.ptype.ptemplate_type import PTemplateType


class PVctrObject(PContainer):
    def __init__(self):
        super(PVctrObject, self).__init__()
        self.type_name = 'PVctrObject'
        self.complete = True

        self.type = PTemplateType('Vctr')
