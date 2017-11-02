from legoc.lexer.types.base_lexer_type import BaseLexerType


class LConstant(BaseLexerType):
    def __init__(self, lexem):
        super(LConstant, self).__init__(lexem)
        self.type_name = 'LConstant'
