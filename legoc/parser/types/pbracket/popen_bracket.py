from legoc.parser.types.pbracket.pbracket import PBracket


class POpenBracket(PBracket):
    def __init__(self, lexem, num=0):
        super(POpenBracket, self).__init__(lexem, num)
        self.type_name = 'POpenBracket'
