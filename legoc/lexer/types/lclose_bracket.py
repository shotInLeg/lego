from legoc.lexer.types.lbracket import LBracketType


class LCloseBracketType(LBracketType):
    def __init__(self, lexem):
        super(LCloseBracketType, self).__init__(lexem)
        self.type_name = 'LCloseBracketType'

        pair = self.get_pair_by_one(self.str_value)
        self.current_number = LBracketType.numbers[pair].pop()
