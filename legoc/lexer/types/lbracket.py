from legoc.lexer.types.base_lexer_type import BaseLexerType


class LBracket(BaseLexerType):
    numbers = {
        '()': [],
        '{}': [],
        '[]': [],
        '<>': []
    }

    max_index = 0

    def __init__(self, lexem):
        super(LBracket, self).__init__(lexem)
        self.type_name = 'LBracket'
        self.current_number = 0

    def __str__(self):
        return '{{{}:{}|{}}}'.format(
            self.type_name,
            self.str_value,
            self.current_number
        )

    @classmethod
    def get_next_index(cls):
        cls.max_index += 1
        return cls.max_index

    def pair(self):
        if self.str_value == '{' or self.str_value == '}':
            return '{}'
        elif self.str_value == '(' or self.str_value == ')':
            return '()'
        elif self.str_value == '[' or self.str_value == ']':
            return '[]'
        elif self.str_value == '<' or self.str_value == '>':
            return '<>'

        return ''
