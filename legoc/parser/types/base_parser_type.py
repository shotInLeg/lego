class BaseParserType(object):
    def __init__(self):
        self.parents = {BaseParserType.__name__}
        self.complete = True

    def left_reduce(self, tkn):
        return None

    def right_reduce(self, tkn):
        return None

    def get(self):
        raise NotImplementedError('Необходимо переопределить метод')

    def __str__(self):
        raise NotImplementedError('Необходимо переопределить метод')
