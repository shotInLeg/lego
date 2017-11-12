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

    @staticmethod
    def get_pair_by_one(one):
        if one == '{' or one == '}':
            return '{}'
        elif one == '(' or one == ')':
            return '()'
        elif one == '[' or one == ']':
            return '[]'
        elif one == '<' or one == '>':
            return '<>'

        return ''

    def pair(self):
        return self.get_pair_by_one(self.str_value)
