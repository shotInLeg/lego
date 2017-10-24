from legoc.parser.types.pbracket.pbracket import PBracket


class PCloseBracket(PBracket):
    def __init__(self, lexem, num):
        super(PCloseBracket, self).__init__(lexem, num)
        self.type_name = 'PCloseBracket'
