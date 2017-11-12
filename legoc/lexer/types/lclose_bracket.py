from legoc.lexer.types.lbracket import LBracket


class LCloseBracket(LBracket):
    def __init__(self, lexem):
        super(LCloseBracket, self).__init__(lexem)
        self.type_name = 'LCloseBracket'

        pair = self.pair()
        self.current_number = LBracket.numbers[pair].pop()
