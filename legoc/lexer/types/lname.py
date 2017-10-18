from legoc.lexer.types.base_lexer_type import BaseLexerType


class LNameType(BaseLexerType):
    def __init__(self, lexem):
        super(LNameType, self).__init__(lexem)
        self.type_name = 'LNameType'
