from legoc.parser.types.base_parser_type import BaseParserType


class PFBrackets(BaseParserType):
    def __init__(self):
        super(PFBrackets, self).__init__()
        self.parents.add(PFBrackets.__name__)

        self.child = None

    def get(self):
        return self

    def __str__(self):
        if isinstance(self.child, list):
            print(type(self.child))
            return 'FB{{{}}}'.format(
                ', '.join([str(x) for x in self.child])
            )

        return 'FB{{{}}}'.format(
            self.child
        )
