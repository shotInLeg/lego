from legoc.parser.types.base_parser_type import BaseParserType


class POperation(BaseParserType):
    bin = [
        '.', '@', '#', ':', '|', '++', '--', '^', '*', '/', '%', '\\', '+',
        '-', '<<', '>>', '<=', '>=', '!=', '==', '||', '&&', '->', '=',
        '+=', '-=', '*=', '/=', '%=', '^=', '\\=', '++=', '--='
    ]
    un_and_bin = ['-']

    un = ['!', '~']

    brac = ['()', '[]', '<>']

    priority = {
        '.': 22, '()': 22, '[]': 22, '<>': 22,

        '!': 21,

        '@': 20, '#': 20,

        '++': 17, '--': 17,

        '^': 15,

        '*': 13, '/': 13, '%': 13, '\\': 13,

        '+': 11, '-': 11,

        '<<': 9, '>>': 9, '<=': 9, '>=': 9,
        '!=': 9, '==': 9, '||': 8, '&&': 8,

        '->': 7,

        '=': 5, '+=': 5, '-=': 5, '*=': 5, '/=': 5,
        '%=': 5, '^=': 5, '\\=': 5, '++=': 5, '--=': 5,

        ':': 4, '|': 4
    }

    def __init__(self, lexeme):
        super(POperation, self).__init__()
        self.tstack.append(POperation.__name__)
        self.complete = False
        self.str_value = lexeme

    def get(self):
        return self
