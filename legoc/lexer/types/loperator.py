from legoc.lexer.types.base_lexer_type import BaseLexerType


class LOperator(BaseLexerType):
    def __init__(self, lexem):
        super(LOperator, self).__init__(lexem)
        self.type_name = 'LOperator'
