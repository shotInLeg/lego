class BaseParserType(object):
    def __init__(self, lexem):
        self.complete = False  # Статус полноценности
        self.type_name = 'BaseParserType'
        self.str_value = lexem

    def __str__(self):
        if self.complete:
            view = '{{{} {}}}'.format(
                self.type_name, self.str_value
            )
        else:
            view = '{{{} {} {}}}'.format(
                self.type_name, self.str_value,
                self.complete
            )

        return view

    def __eq__(self, b):
        return self.type_name == b.type_name and \
               self.str_value == b.str_value and \
               self.complete == self.complete
