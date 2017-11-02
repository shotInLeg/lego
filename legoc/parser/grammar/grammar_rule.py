# config: utf-8
from legoc.parser.types import *


class GrammarRule(object):
    def __init__(self, *tpl):
        self.tpl = tuple([x for x in tpl])
        self.current_index = -1

    def __str__(self):
        return 'GR({})'.format(
            ', '.join(
                str(x) for x in self.tpl
            )
        )

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1

        if self.current_index >= len(self.tpl):
            self.current_index = -1
            raise StopIteration

        return self.tpl.__getitem__(self.current_index)

    def __len__(self):
        return self.tpl.__len__()

    def __hash__(self):
        return self.tpl.__hash__()

    def __eq__(self, other):
        if type(other) == GrammarRule:
            if len(self) != len(other):
                return False

            equals = []
            for item_s, item_o in zip(self.tpl, other.tpl):

                # Допустим пришли 2 типа
                if self.type_eq_type(item_s, item_o) == 1:
                    equals.append(True)
                    continue

                elif self.type_eq_type(item_s, item_o) == 0:
                    equals.append(False)
                    continue

                # Допустим пришел один объект и один тип
                elif self.type_eq_obj(item_s, item_o) == 1:
                    equals.append(True)
                    continue

                elif self.type_eq_obj(item_s, item_o) == 0:
                    equals.append(False)
                    continue

                # Допустим пришли пришли объекты
                elif self.obj_eq_obj(item_s, item_o) == 1:
                    equals.append(True)
                    continue

                elif self.obj_eq_obj(item_s, item_o) == 0:
                    equals.append(False)
                    continue

            if len(equals) != len(self):
                raise ValueError('Переданны не корректные данные')

            # Если хотябы один False - Вернуть False
            if [x for x in equals if not x]:
                return False
            return True

    @staticmethod
    def type_eq_type(type1, type2):
        """
        Equal 2 types
        :return:
            1 - equal
            0 - not equal
            -1 - is not type
        """
        try:
            if issubclass(type1, BaseParserType) and \
                    issubclass(type2, BaseParserType):
                if issubclass(type1, type2) or issubclass(type2, type1):
                    return 1
            return 0
        except TypeError:
            return -1

    @staticmethod
    def type_eq_obj(type_obj1, type_obj2):
        """
        Equal type and object
        :return:
            1 - equal
            0 - not equal
            -1 - is not type
        """
        try:
            if issubclass(type_obj1, BaseParserType):
                if isinstance(type_obj2, type_obj1):
                    return 1
            return 0
        except TypeError:
            try:
                if issubclass(type_obj2, BaseParserType):
                    if isinstance(type_obj1, type_obj2):
                        return 1
                return 0
            except TypeError:
                return -1

    @staticmethod
    def obj_eq_obj(obj1, obj2):
        """
        Equal 2 objects
        :return:
            1 - equal
            0 - not equal
        """
        if isinstance(obj1, BaseParserType) and \
                isinstance(obj2, BaseParserType):
            if obj1 == obj2:
                return 1
        return 0
