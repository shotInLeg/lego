class BaseLexerType(object):
    def __init__(self):
        self._type = 'BaseLexerType'
        self._str_view = 'None'

    def __str__(self):
        return '{{{}:{}}}'.format(self._type, self._str_view)
