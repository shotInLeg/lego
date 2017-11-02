from legoc.parser.types import *
from legoc.parser.grammar.grammar_rule import GrammarRule


grammar = [
    # Dict
    (GrammarRule(POpenBracket('['), PManageOperation(':'), PCloseBracket(']')), PDictObject.bob),
    (GrammarRule(POpenBracket('['), PAssociativePair, PCloseBracket(']')), PDictObject.bpb),
    (GrammarRule(POpenBracket('['), PAssociativePairList, PCloseBracket(']')), PDictObject.bplb),

    # Vector
    (GrammarRule(POpenBracket('['), PCloseBracket(']')), PVctrObject.bb),
    (GrammarRule(POpenBracket('['), PValue, PCloseBracket(']')), PVctrObject.bvb),
    (GrammarRule(POpenBracket('['), PExpressionList, PCloseBracket(']')), PVctrObject.belb),

    # Struct
    (GrammarRule(POpenBracket('['), PAssignOperation, PCloseBracket(']')), PStrctObject.bab),
    (GrammarRule(POpenBracket('['), PDefine, PCloseBracket(']')), PStrctObject.bdb),
    (GrammarRule(POpenBracket('['), PDefineList, PCloseBracket(']')), PStrctObject.bdlb),

    # Formal params
    (GrammarRule(POpenBracket('('), PCloseBracket(')')), PFormalParams.bb),
    (GrammarRule(POpenBracket('('), PName, PCloseBracket(')')), PFormalParams.bnb),
    (GrammarRule(POpenBracket('('), PNameList, PCloseBracket(')')), PFormalParams.bnlb),

    # Fact params
    (GrammarRule(POpenBracket('('), PExpression, PCloseBracket(')')), PFactParams.beb),
    (GrammarRule(POpenBracket('('), PValue, PCloseBracket(')')), PFactParams.bvb),
    (GrammarRule(POpenBracket('('), PExpressionList, PCloseBracket(')')), PFactParams.belb),

    # Function type
    (GrammarRule(PType, POpenBracket('('), PCloseBracket(')')), PFuncType.tbb),
    (GrammarRule(PType, POpenBracket('('), PType, PCloseBracket(')')), PFuncType.tbtb),
    (GrammarRule(PType, POpenBracket('('), PTypeList, PCloseBracket(')')), PFuncType.tbtlb),

    # Pair
    (GrammarRule(PValue, PManageOperation(':'), PValue), PAssociativePair.vov),

    # Expression
    (GrammarRule(PValue, PImmutableOperation, PValue), PExpression.vov),

    # AssociativePair List
    (GrammarRule(PAssociativePairList, POperator(','), PAssociativePair), PAssociativePairList.plod),
    (GrammarRule(PAssociativePair, POperator(','), PAssociativePair), PAssociativePairList.apoap),

    # Assign variable
    (GrammarRule(PName, PAssignOperation, PRValue), PDefineVar.noc),
    (GrammarRule(PName, PAssignOperation, PSimpleType, PValue), PDefineVar.notr),

    # Assign function
    (GrammarRule(PName, PFormalParams, PAssignOperation, PValue), PDefineFunc.nfov),
    (GrammarRule(PName, PFormalParams, PAssignOperation, PFuncType, PValue), PDefineFunc.nfotv),

    # Name List
    (GrammarRule(PNameList, POperator(','), PName), PNameList.lon),
    (GrammarRule(PName, POperator(','), PName), PNameList.non),

    # Type List
    (GrammarRule(PTypeList, POperator(','), PType), PTypeList.lot),
    (GrammarRule(PType, POperator(','), PType), PTypeList.tot),

    # Expression List
    (GrammarRule(PNameList, POperator(','), PValue), PExpressionList.eov),
    (GrammarRule(PValue, POperator(','), PNameList), PExpressionList.voe),
    (GrammarRule(PExpressionList, POperator(','), PValue), PExpressionList.eov),
    (GrammarRule(PValue, POperator(','), PValue), PExpressionList.vov),

    # Define List
    (GrammarRule(PDefineList, POperator(','), PDefine), PDefineList.dlod),
    (GrammarRule(PDefine, POperator(','), PDefine), PDefineList.dod),

    # Instruction
    (GrammarRule(BaseParserType, POperator(';')), PInstruction.bo)
]
