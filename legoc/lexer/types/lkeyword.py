from legoc.lexer.types.base_lexer_type import BaseLexerType


class LKeywordType(BaseLexerType):
    def __init__(self):
        super(LKeywordType, self).__init__()
        self._type = 'LKeywordType'
        self._str_view = 'None'
