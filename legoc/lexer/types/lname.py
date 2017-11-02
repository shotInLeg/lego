from legoc.lexer.types.base_lexer_type import BaseLexerType


class LName(BaseLexerType):
    def __init__(self, lexem):
        super(LName, self).__init__(lexem)
        self.type_name = 'LName'
