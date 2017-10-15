from legoc.lexer.types.base_lexer_type import BaseLexerType


class LTypeType(BaseLexerType):
    def __init__(self):
        super(LTypeType, self).__init__()
        self._type = 'LTypeType'
        self._str_view = 'None'
