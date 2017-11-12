class BaseParserType(object):
    def __init__(self):
        self.tstack = [BaseParserType.__name__]
        self.complete = True

    def get(self):
        raise NotImplementedError('Функцию необходимо переопределить')
