from legoc.lexer.types.base_lexer_type import BaseLexerType


class LBracketType(BaseLexerType):
    number = 0

    def __init__(self, lexem):
        super(LBracketType, self).__init__(lexem)
        self._type = 'LBracketType'
        self._current_number = 0

    def __str__(self):
        return '{{{}:{}|{}}}'.format(
            self._type,
            self._str_view,
            self._current_number
        )
