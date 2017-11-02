from legoc.parser.types.pbracket.pbracket import PBracket


class PCloseBracket(PBracket):
    def __init__(self, lexem, num=0):
        super(PCloseBracket, self).__init__(lexem, num)
        self.type_name = 'PCloseBracket'
