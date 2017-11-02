from legoc.lexer.types.lbracket import LBracket


class LOpenBracket(LBracket):
    def __init__(self, lexem):
        super(LOpenBracket, self).__init__(lexem)
        self.type_name = 'LOpenBracket'

        self.current_number = self.get_next_index()
        pair = self.get_pair_by_one(self.str_value)
        LOpenBracket.numbers[pair].append(self.current_number)
