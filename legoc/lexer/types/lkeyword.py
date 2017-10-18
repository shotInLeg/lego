from legoc.lexer.types.base_lexer_type import BaseLexerType


class LKeywordType(BaseLexerType):
    def __init__(self, lexem):
        super(LKeywordType, self).__init__(lexem)
        self.type_name = 'LKeywordType'
