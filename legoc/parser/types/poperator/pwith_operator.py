from legoc.parser.types.poperator.pcontext_operator import PContextOperator


class PWithOperator(PContextOperator):
    def __init__(self, lexem):
        super(PWithOperator, self).__init__(lexem)
        self.type_name = 'PWithOperator'
        self.complete = True
