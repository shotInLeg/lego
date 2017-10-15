from legoc.lexer.types.base_lexer_type import BaseLexerType


class LOperationType(BaseLexerType):
    def __init__(self):
        super(LOperationType, self).__init__()
        self._type = 'LOperationType'
        self._str_view = 'None'
