class BaseLexerType(object):
    def __init__(self, lexem):
        self._type = 'BaseLexerType'
        self._str_view = lexem

    def __str__(self):
        return '{{{}:{}}}'.format(self._type, self._str_view)

    def __eq__(self, b):
        return self._type == b._type and \
               self._str_view == b._str_view
