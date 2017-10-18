from legoc.lexer.types.base_lexer_type import BaseLexerType


class LOperatorType(BaseLexerType):
    def __init__(self, lexem):
        super(LOperatorType, self).__init__(lexem)
        self.type_name = 'LOperatorType'
