from legoc.lexer.types.base_lexer_type import BaseLexerType


class LNameType(BaseLexerType):
    def __init__(self):
        super(LNameType, self).__init__()
        self._type = 'LNameType'
        self._str_view = 'None'
