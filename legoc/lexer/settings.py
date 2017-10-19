import re

from legoc.lexer.types import *


lkeyword_priority = 7
loperator_priority = 6
loperation_priority = 5
ltype_priority = 4
lbracket_priority = 3
lvalue_priority = 2
lname_priority = 1


regexp = {
    re.compile(r'^cnst$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^priv$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^prot$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^publ$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^read$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^write$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^clr'): ('lkeyword', lkeyword_priority),

    re.compile(r'^[a-z]$'): ('lname', lname_priority),
    re.compile(r'^[a-z][A-Za-z0-9]+$'): ('lname', lname_priority),

    re.compile(r'^[+]$'): ('loperation', loperation_priority),
    re.compile(r'^[-]$'): ('loperation', loperation_priority),
    re.compile(r'^[*]$'): ('loperation', loperation_priority),
    re.compile(r'^[/]$'): ('loperation', loperation_priority),
    re.compile(r'^[%]$'): ('loperation', loperation_priority),
    re.compile(r'^[=]$'): ('loperation', loperation_priority),
    re.compile(r'^[<]$'): ('loperation', loperation_priority),
    re.compile(r'^[>]$'): ('loperation', loperation_priority),
    re.compile(r'^[<][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[>][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[=][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[!][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[!]$'): ('loperation', loperation_priority),
    re.compile(r'^[+][+]$'): ('loperation', loperation_priority),
    re.compile(r'^[-][-]$'): ('loperation', loperation_priority),
    re.compile(r'^[+][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[-][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[*][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[/][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[%][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[+][+][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[-][-][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[-][>]$'): ('loperation', loperation_priority),
    re.compile(r'^[.]$'): ('loperation', loperation_priority),
    re.compile(r'^in$'): ('loperation', loperation_priority),
    re.compile(r'^is$'): ('loperation', loperation_priority),

    re.compile(r'^[\(]$'): ('lopen_bracket', lbracket_priority),
    re.compile(r'^[\)]$'): ('lclose_bracket', lbracket_priority),
    re.compile(r'^[\[]$'): ('lopen_bracket', lbracket_priority),
    re.compile(r'^[\]]$'): ('lclose_bracket', lbracket_priority),
    re.compile(r'^[\{]$'): ('lopen_bracket', lbracket_priority),
    re.compile(r'^[\}]$'): ('lclose_bracket', lbracket_priority),
    re.compile(r'^[\<]$'): ('lopen_bracket', lbracket_priority),
    re.compile(r'^[\>]$'): ('lclose_bracket', lbracket_priority),

    re.compile(r'^if$'): ('loperator', loperator_priority),
    re.compile(r'^elif$'): ('loperator', loperator_priority),
    re.compile(r'^else$'): ('loperator', loperator_priority),
    re.compile(r'^while$'): ('loperator', loperator_priority),
    re.compile(r'^for$'): ('loperator', loperator_priority),
    re.compile(r'^do$'): ('loperator', loperator_priority),
    re.compile(r'^with$'): ('loperator', loperator_priority),
    re.compile(r'^return$'): ('loperator', loperator_priority),
    re.compile(r'^throw'): ('loperator', loperator_priority),
    re.compile(r'^try'): ('loperator', loperator_priority),
    re.compile(r'^catch'): ('loperator', loperator_priority),
    re.compile(r'^finally'): ('loperator', loperator_priority),
    re.compile(r'^[,]$'): ('loperator', loperator_priority),
    re.compile(r'^[;]$'): ('loperator', loperator_priority),

    re.compile(r'^[A-Z]$'): ('ltype', ltype_priority),
    re.compile(r'^[A-Z][A-Za-z0-9]+$'): ('ltype', ltype_priority),

    re.compile(r'^[T][_]$'): ('ltype', ltype_priority),
    re.compile(r'^[T][_][A-Z0-9]$'): ('ltype', ltype_priority),
    re.compile(r'^[T][_][A-Z0-9][A-Za-z0-9]+$'): ('ltype', ltype_priority),

    re.compile(r'^[0-9]$'):
        ('lvalue', lvalue_priority),  # number (1)
    re.compile(r'^([0-9][_]?)+$'):
        ('lvalue', lvalue_priority),  # number (1_0)
    re.compile(r'^([0-9][_]?)+[.]([0-9][_]?)+$'):
        ('lvalue', lvalue_priority),  # number (1_000.000_23)
    re.compile(r'^([0-9][_]?)+[.]$'):
        ('lvalue', lvalue_priority),  # number (1_000.)

    re.compile(r'^\".*\"$'): ('lvalue', lvalue_priority),  # string
}


ltypes = {
    'lkeyword': LKeywordType,
    'lname': LNameType,
    'loperation': LOperationType,
    'loperator': LOperatorType,
    'ltype': LTypeType,
    'lopen_bracket': LOpenBracketType,
    'lclose_bracket': LCloseBracketType,
    'lvalue': LValueType
}
