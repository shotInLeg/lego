from legoc.lexer.types.base_lexer_type import BaseLexerType


class LOperatorType(BaseLexerType):
    def __init__(self):
        super(LOperatorType, self).__init__()
        self._type = 'LOperatorType'
        self._str_view = 'None'
