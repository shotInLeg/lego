from legoc.model.types.base_model_type import BaseModelType


class MInit(BaseModelType):
    def __init__(self):
        super(MInit, self).__init__()
        self.tstack.append(MInit.__name__)
