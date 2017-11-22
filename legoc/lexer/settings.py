import re

from legoc.lexer.types import *


lkeyword_priority = 8
lmodifier_priority = 7
loperator_priority = 6
loperation_priority = 5
ltype_priority = 4
lbracket_priority = 3
lconstant_priority = 2
lname_priority = 1


regexp = {
    re.compile(r'^package$'): ('lkeyword', lkeyword_priority),
    re.compile(r'^using'): ('lkeyword', lkeyword_priority),
    re.compile(r'^import'): ('lkeyword', lkeyword_priority),

    re.compile(r'^cnst$'): ('lmodifier', lmodifier_priority),
    re.compile(r'^priv$'): ('lmodifier', lmodifier_priority),
    re.compile(r'^prot$'): ('lmodifier', lmodifier_priority),
    re.compile(r'^publ$'): ('lmodifier', lmodifier_priority),
    re.compile(r'^clr'): ('lmodifier', lmodifier_priority),

    re.compile(r'^[a-z]$'): ('lname', lname_priority),
    re.compile(r'^[a-z][A-Za-z0-9]+$'): ('lname', lname_priority),

    re.compile(r'^[+]$'): ('loperation', loperation_priority),
    re.compile(r'^[-]$'): ('loperation', loperation_priority),
    re.compile(r'^[*]$'): ('loperation', loperation_priority),
    re.compile(r'^[/]$'): ('loperation', loperation_priority),
    re.compile(r'^[%]$'): ('loperation', loperation_priority),
    re.compile(r'^[=]$'): ('loperation', loperation_priority),
    re.compile(r'^[=][\>]$'): ('loperation', loperation_priority),
    re.compile(r'^[<][<]$'): ('loperation', loperation_priority),
    re.compile(r'^[>][>]$'): ('loperation', loperation_priority),
    re.compile(r'^[<][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[>][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[=][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[!][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[!]$'): ('loperation', loperation_priority),
    re.compile(r'^[&][&]$'): ('loperation', loperation_priority),
    re.compile(r'^[|][|]$'): ('loperation', loperation_priority),
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
    re.compile(r'^[:]$'): ('loperation', loperation_priority),
    re.compile(r'^[|]$'): ('loperation', loperation_priority),
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
    re.compile(r'^throw$'): ('loperator', loperator_priority),
    re.compile(r'^try$'): ('loperator', loperator_priority),
    re.compile(r'^catch$'): ('loperator', loperator_priority),
    re.compile(r'^finally$'): ('loperator', loperator_priority),
    re.compile(r'^[,]$'): ('loperator', loperator_priority),
    re.compile(r'^[;]$'): ('loperator', loperator_priority),

    re.compile(r'^[A-Z]$'): ('ltype', ltype_priority),
    re.compile(r'^[A-Z][A-Za-z0-9]+$'): ('ltype', ltype_priority),

    re.compile(r'^[T][_]$'): ('ltype', ltype_priority),
    re.compile(r'^[T][_][A-Z0-9]$'): ('ltype', ltype_priority),
    re.compile(r'^[T][_][A-Z0-9][A-Za-z0-9]+$'): ('ltype', ltype_priority),

    re.compile(r'^[0-9]$'):
        ('lconstant', lconstant_priority),  # number (1)
    re.compile(r'^([0-9][_]?)+$'):
        ('lconstant', lconstant_priority),  # number (1_0)
    re.compile(r'^([0-9][_]?)+[.]([0-9][_]?)+$'):
        ('lconstant', lconstant_priority),  # number (1_000.000_23)
    re.compile(r'^([0-9][_]?)+[.]$'):
        ('lconstant', lconstant_priority),  # number (1_000.)

    re.compile(r'^\".*\"$'): ('lconstant', lconstant_priority),  # string
    re.compile(r'^\'.*\'$'): ('lconstant', lconstant_priority),  # insertion

    re.compile(r'^true$'): ('lconstant', lconstant_priority),  # bool
    re.compile(r'^false$'): ('lconstant', lconstant_priority),  # bool
}


ltypes = {
    'lkeyword': LKeyword,
    'lmodifier': LModifier,
    'lname': LName,
    'loperation': LOperation,
    'loperator': LOperator,
    'ltype': LType,
    'lopen_bracket': LOpenBracket,
    'lclose_bracket': LCloseBracket,
    'lconstant': LConstant
}
