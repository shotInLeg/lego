from legoc.lexer.types.base_lexer_type import BaseLexerType


class LType(BaseLexerType):
    def __init__(self, lexem):
        super(LType, self).__init__(lexem)
        self.type_name = 'LType'
