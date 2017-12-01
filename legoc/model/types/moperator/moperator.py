from legoc.model.types.base_model_type import BaseModelType


class MOperator(BaseModelType):
    def __init__(self):
        super(MOperator, self).__init__()
        self.tstack.append(MOperator.__name__)
