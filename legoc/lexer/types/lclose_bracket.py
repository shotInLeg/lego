from legoc.lexer.types.lbracket import LBracket


class LCloseBracket(LBracket):
    def __init__(self, lexem):
        super(LCloseBracket, self).__init__(lexem)
        self.type_name = 'LCloseBracket'

        pair = self.get_pair_by_one(self.str_value)
        self.current_number = LBracket.numbers[pair].pop()
