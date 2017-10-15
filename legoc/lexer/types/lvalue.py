from legoc.lexer.types.base_lexer_type import BaseLexerType


class LValueType(BaseLexerType):
    def __init__(self):
        super(LValueType, self).__init__()
        self._type = 'LValueType'
        self._str_view = 'None'
