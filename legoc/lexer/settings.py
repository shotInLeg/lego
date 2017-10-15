import re

from legoc.lexer.types import *

lkeyword_priority = 6
loperator_priority = 5
loperation_priority = 4
ltype_priority = 3
lvalue_priority = 2
lname_priority = 1

regexp = {
    re.compile(r'^let$'): ('lkeyword', lkeyword_priority),

    re.compile(r'^[a-z][A-Za-z0-9]+$'): ('lname', lname_priority),
    re.compile(r'^[a-z]$'): ('lname', lname_priority),

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
    re.compile(r'^[+][+]$'): ('loperation', loperation_priority),
    re.compile(r'^[-][-]$'): ('loperation', loperation_priority),
    re.compile(r'^[+][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[-][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[*][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[/][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[%][=]$'): ('loperation', loperation_priority),
    re.compile(r'^[(]$'): ('loperation', loperation_priority),
    re.compile(r'^[)]$'): ('loperation', loperation_priority),
    re.compile(r'^[[]$'): ('loperation', loperation_priority),
    re.compile(r'^[]]$'): ('loperation', loperation_priority),
    re.compile(r'^[{]$'): ('loperation', loperation_priority),
    re.compile(r'^[}]$'): ('loperation', loperation_priority),
    re.compile(r'^in$'): ('loperation', loperation_priority),
    re.compile(r'^is$'): ('loperation', loperation_priority),

    re.compile(r'^if$'): ('loperator', loperator_priority),
    re.compile(r'^elif$'): ('loperator', loperator_priority),
    re.compile(r'^else$'): ('loperator', loperator_priority),
    re.compile(r'^while$'): ('loperator', loperator_priority),
    re.compile(r'^for$'): ('loperator', loperator_priority),
    re.compile(r'^do$'): ('loperator', loperator_priority),
    re.compile(r'^return$'): ('loperator', loperator_priority),

    re.compile(r'^[A-Z][A-Za-z0-9_<>]+$'): ('ltype', ltype_priority),
    re.compile(r'^[A-Z]$'): ('ltype', ltype_priority),
    re.compile(r'^[A-Z][A-Za-z0-9_<>]+\(.*\)$'): ('ltype', ltype_priority),
    re.compile(r'^[A-Z]\(.*\)$'): ('ltype', ltype_priority),

    re.compile(r'^[0-9][0-9._]+[0-9]$'): ('lvalue', lvalue_priority),  # number
    re.compile(r'^[0-9]+[0-9]$'): ('lvalue', lvalue_priority),  # number
    re.compile(r'^[0-9]$'): ('lvalue', lvalue_priority),  # number
    re.compile(r'^\".*\"$'): ('lvalue', lvalue_priority),  # string
}


ltypes = {
    'lkeyword': LKeywordType,
    'lname': LNameType,
    'loperation': LOperationType,
    'loperator': LOperatorType,
    'ltype': LTypeType,
    'lvalue': LValueType
}
