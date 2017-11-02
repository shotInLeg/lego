import re

from legoc.lexer.types import *
from legoc.parser.types import *


constants_ptrns = {
    re.compile(r'^[0-9]$'): PIntConstant,
    re.compile(r'^([0-9][_]?)+$'): PIntConstant,
    re.compile(r'^([0-9][_]?)+[.]([0-9][_]?)+$'): PDblConstant,
    re.compile(r'^([0-9][_]?)+[.]$'): PDblConstant,
    re.compile(r'^\".*\"$'): PStrConstant
}


operation_class = {
    ('=',): PAssignOperation,

    ('+', '-', '*', '/', '%', '\\', '^'): PMathOperation,
    ('<', '>', '<=', '>=', '!=', '==', '||', '&&', '!'): PLogicOperation,
    ('++', '--', '@', '#', ':', '.', '->'): PManageOperation,

    ('+=', '-=', '*=', '/=', '%=', '\\=', '^='): PMutMathOperation,
    ('++=', '--='): PMutManageOperation,
}


operation_priority = {
    '@': 20, '#': 20, ':': 20, '.': 20,

    '++': 17, '--': 17,

    '^': 15,

    '*': 13, '/': 13, '%': 13, '\\': 13,

    '+': 11, '-': 11,

    '<': 9, '>': 9, '<=': 9, '>=': 9,
    '!=': 9, '==': 9, '||': 8, '&&': 8, '!': 8,

    '->': 7,

    '=': 5, '+=': 5, '-=': 5, '*=': 5, '/=': 5,
    '%=': 5, '^=': 5, '\\=': 5, '++=': 5, '--=': 5
}


def ptype_constr(ltype):
    return PSimpleType(ltype.str_value)


def pname_constr(lname):
    return PName(lname.str_value)


def pconstant_constr(lconstant):
    for ptrn, pconstant_type in constants_ptrns.items():
        if ptrn.match(lconstant.str_value):
            return pconstant_type(lconstant.str_value)
    return None


def poperation_constr(loperation):
    for lst, poperation_type in operation_class.items():
        if loperation.str_value in lst:
            return poperation_type(loperation.str_value)
    return None


def poperator_constr(loperator):
    return POperator(loperator.str_value)


def pbracket_constr(lbracket):
    if isinstance(lbracket, LOpenBracket):
        return POpenBracket(lbracket.str_value, lbracket.current_number)
    elif isinstance(lbracket, LCloseBracket):
        return PCloseBracket(lbracket.str_value, lbracket.current_number)
    return None


def pkeyword_constr(lkeyword):
    return PKeyword(lkeyword.str_value)
