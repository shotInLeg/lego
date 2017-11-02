from legoc.parser.grammar.grammar import grammar
from legoc.parser.grammar.grammar_rule import GrammarRule
from legoc.parser.settings import token_mapping


class Parser(object):
    def run(self, lexer_tokens):
        parser_tokens = [self.get_token(x) for x in lexer_tokens]

        rule_num = 0
        while rule_num < len(grammar):
            rule, constr = grammar[rule_num]

            token_num = 0
            while token_num < len(parser_tokens):
                match_len = len(rule)

                if token_num+match_len-1 < len(parser_tokens):
                    slice = GrammarRule(
                        *parser_tokens[token_num:token_num+match_len]
                    )

                    if slice == rule:
                        parser_tokens = self.reorganize(
                            parser_tokens,
                            token_num,
                            token_num+match_len,
                            slice,
                            constr
                        )

                        rule_num = -1
                        break

                token_num += 1
            rule_num += 1

        return parser_tokens

    def reorganize(self, tokens, si, ei, slice, construct):
        left_part = []

        i = 0
        while i < len(tokens) and i != si:
            left_part.append(tokens[i])
            i += 1

        right_part = []

        i = ei
        while i < len(tokens):
            right_part.append(tokens[i])
            i += 1

        new_token = construct(*slice)
        new_tokens = []
        new_tokens.extend(left_part)
        new_tokens.append(new_token)
        new_tokens.extend(right_part)

        return new_tokens

    def get_token(self, ltoken):
        for token_type, constr in token_mapping.items():
            if isinstance(ltoken, token_type):
                return constr(ltoken)
        return None

    @staticmethod
    def aplicate(stack, token):
        current_stack_state = stack[::]
        work_stack = stack[::]
        work_stack.append(token)

        while current_stack_state != work_stack and len(work_stack) > 1:
            current_stack_state = work_stack[::]

            item_l = work_stack.pop(-1)
            item_pl = work_stack.pop(-1)
            item_new = Parser.reduce2(item_pl, item_l)

            if item_new is None:
                work_stack.append(item_pl)
                work_stack.append(item_l)

            else:
                work_stack.append(item_new)

        return work_stack

    @staticmethod
    def reduce2(item_pl, item_l):
        item_new = None

        if item_pl.ra:
            item_new = item_pl.right_reduce(item_l)

        if item_l.la and item_new is None and item_pl.complete:
            item_new = item_l.left_reduce(item_pl)

        return item_new
