from legoc.lexer.types.lbracket import LBracketType


class LOpenBracketType(LBracketType):
    def __init__(self, lexem):
        super(LOpenBracketType, self).__init__(lexem)
        self._type = 'LOpenBracketType'

        LBracketType.number += 1
        self._current_number = LBracketType.number
