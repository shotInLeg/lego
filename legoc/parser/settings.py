from legoc.lexer.types import *
from legoc.parser.types import *


classes_mapping = {
    LType: PSimpleType,
    LName: PName,
    LConstant: PConstant,
    LModifier: PModifier,
    LKeyword: PKeyword
}
