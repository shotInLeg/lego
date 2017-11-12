from legoc.lexer.types import *
from legoc.parser.types import *


token_mapping = {
    LType: PType,
    LName: PName,
    LConstant: PConstant,
    LOperation: PBOperation,
    LKeyword: PModifier
}
