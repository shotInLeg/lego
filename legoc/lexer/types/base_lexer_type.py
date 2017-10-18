class BaseLexerType(object):
    def __init__(self, lexem):
        self.type_name = 'BaseLexerType'
        self.str_value = lexem

    def __str__(self):
        return '{{{}:{}}}'.format(
            self.type_name, self.str_value
        )

    def __eq__(self, b):
        return self.type_name == b.type_name and \
               self.str_value == b.str_value
