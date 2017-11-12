from legoc.parser.types.base_parser_type import BaseParserType


class PModifier(BaseParserType):
    def __init__(self, lexeme):
        super(PModifier, self).__init__()
        self.parents.add(PModifier.__name__)
        self.str_value = lexeme

    def get(self):
        return self

    def right_reduce(self, tkn):
        if 'PInit' in tkn.get().parents:
            tkn.get().modifiers.append(self)
            return tkn
        return None

    def __str__(self):
        return 'Mod {}'.format(
            self.str_value
        )
