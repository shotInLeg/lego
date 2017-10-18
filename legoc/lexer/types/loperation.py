from legoc.lexer.types.base_lexer_type import BaseLexerType


class LOperationType(BaseLexerType):
    def __init__(self, lexem):
        super(LOperationType, self).__init__(lexem)
        self.type_name = 'LOperationType'
