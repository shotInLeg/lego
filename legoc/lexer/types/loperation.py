from legoc.lexer.types.base_lexer_type import BaseLexerType


class LOperation(BaseLexerType):
    def __init__(self, lexem):
        super(LOperation, self).__init__(lexem)
        self.type_name = 'LOperation'
