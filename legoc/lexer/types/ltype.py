from legoc.lexer.types.base_lexer_type import BaseLexerType


class LTypeType(BaseLexerType):
    def __init__(self, lexem):
        super(LTypeType, self).__init__(lexem)
        self.type_name = 'LTypeType'
