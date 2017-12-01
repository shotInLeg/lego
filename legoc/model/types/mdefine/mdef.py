from legoc.model.types.base_model_type import BaseModelType


class MDef(BaseModelType):
    def __init__(self):
        super(MDef, self).__init__()
        self.tstack.append(MDef.__name__)
