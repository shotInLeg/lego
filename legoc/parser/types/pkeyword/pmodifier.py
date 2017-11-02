from legoc.parser.types.pkeyword.pkeyword import PKeyword


class PModifier(PKeyword):
    def __init__(self, lexem):
        super(PKeyword, self).__init__(lexem)
        self.type_name = 'PKeyword'
        self.complete = True
