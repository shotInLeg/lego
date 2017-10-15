from legoc.lexer.types.base_lexer_type import BaseLexerType


class LValueType(BaseLexerType):
    def __init__(self, lexem):
        super(LValueType, self).__init__(lexem)
        self._type = 'LValueType'
