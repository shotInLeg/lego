from legoc.lexer.types.lbracket import LBracketType


class LOpenBracketType(LBracketType):
    def __init__(self, lexem):
        super(LOpenBracketType, self).__init__(lexem)
        self.type_name = 'LOpenBracketType'

        self.current_number = self.get_next_index()
        pair = self.get_pair_by_one(self.str_value)
        LBracketType.numbers[pair].append(self.current_number)
