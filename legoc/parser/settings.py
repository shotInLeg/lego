from legoc.lexer.types import *
from legoc.parser.constructors import (
    ptype_constr, pname_constr, pconstant_constr,
    poperation_constr, poperator_constr, pbracket_constr,
    pkeyword_constr
)


token_mapping = {
    LType: ptype_constr,
    LName: pname_constr,
    LConstant: pconstant_constr,
    LOperation: poperation_constr,
    LOperator: poperator_constr,
    LBracket: pbracket_constr,
    LKeyword: pkeyword_constr
}
