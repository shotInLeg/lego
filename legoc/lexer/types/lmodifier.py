from legoc.lexer.types.base_lexer_type import BaseLexerType


class LModifier(BaseLexerType):
    def __init__(self, lexem):
        super(LModifier, self).__init__(lexem)
        self.type_name = 'LModifier'
