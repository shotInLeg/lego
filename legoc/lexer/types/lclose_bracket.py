from legoc.lexer.types.lbracket import LBracketType


class LCloseBracketType(LBracketType):
    def __init__(self, lexem):
        super(LCloseBracketType, self).__init__(lexem)
        self._type = 'LCloseBracketType'

        self._current_number = LBracketType.number
        LBracketType.number -= 1
