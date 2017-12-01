from legoc.model.types.base_model_type import BaseModelType


class MExp(BaseModelType):
    def __init__(self, pexp):
        super(MExp, self).__init__()
        self.tstack.append(MExp.__name__)

        self.pexp = pexp
