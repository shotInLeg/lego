from legoc.lexer.types.base_lexer_type import BaseLexerType


class LKeyword(BaseLexerType):
    def __init__(self, lexem):
        super(LKeyword, self).__init__(lexem)
        self.type_name = 'LKeyword'
