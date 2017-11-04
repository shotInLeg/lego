from legoc.parser.types import *
from legoc.parser.grammar.grammar_rule import GrammarRule


grammar = [
    # DATA STRUCTURES

    # Dict
    (GrammarRule(POpenBracket('['), PManageOperation(':'), PCloseBracket(']')), PDictObject.b_o_b),
    (GrammarRule(POpenBracket('['), PAssociativePair, PCloseBracket(']')), PDictObject.b_item_b),
    (GrammarRule(POpenBracket('['), PAssociativePairList, PCloseBracket(']')), PDictObject.b_itemlist_b),

    # Vector
    (GrammarRule(POpenBracket('['), PCloseBracket(']')), PVctrObject.b_b),
    (GrammarRule(POpenBracket('['), PValue, PCloseBracket(']')), PVctrObject.b_item_b),
    (GrammarRule(POpenBracket('['), PExpressionList, PCloseBracket(']')), PVctrObject.b_itemlist_b),

    # Struct
    (GrammarRule(POpenBracket('['), PAssignOperation, PCloseBracket(']')), PStrctObject.b_o_b),
    (GrammarRule(POpenBracket('['), PInit, PCloseBracket(']')), PStrctObject.b_item_b),
    (GrammarRule(POpenBracket('['), PInitList, PCloseBracket(']')), PStrctObject.b_itemlist_b),

    # COMPLEX TYPES

    # Function type
    (GrammarRule(PType, POpenBracket('('), PCloseBracket(')')), PFuncType.type_b_b),
    (GrammarRule(PType, POpenBracket('('), PType, PCloseBracket(')')), PFuncType.type_b_type_b),
    (GrammarRule(PType, POpenBracket('('), PTypeList, PCloseBracket(')')), PFuncType.type_b_typelist_b),

    (GrammarRule(PType, PLogicOperation('<'), PLogicOperation('>')), PTemplateType.type_b_b),
    (GrammarRule(PType, PLogicOperation('<'), PType, PLogicOperation('>')), PTemplateType.type_b_type_b),
    (GrammarRule(PType, PLogicOperation('<'), PTypeList, PLogicOperation('>')), PTemplateType.type_b_typelist_b),

    # UNFORMAL STRUCTURES

    # Unary Operation
    (GrammarRule(POpenBracket('('), PImmutableOperation, PValue, PCloseBracket(')')), PUnaryOperation.b_operation_item_b),

    # Context
    (GrammarRule(POpenBracket('{'), PValue, PCloseBracket('}')), PContext.b_item_b),
    (GrammarRule(POpenBracket('{'), PInstruction, PCloseBracket('}')), PContext.b_item_b),
    (GrammarRule(POpenBracket('{'), PInstructionList, PCloseBracket('}')), PContext.b_itemlist_b),

    # Formal params
    (GrammarRule(POpenBracket('('), PCloseBracket(')')), PFormalParams.b_b),
    (GrammarRule(POpenBracket('('), PName, PCloseBracket(')')), PFormalParams.b_item_b),
    (GrammarRule(POpenBracket('('), PNameList, PCloseBracket(')')), PFormalParams.b_itemlist_b),

    # Fact params
    (GrammarRule(POpenBracket('('), PValue, PCloseBracket(')')), PFactParams.b_item_b),
    (GrammarRule(POpenBracket('('), PParams, PCloseBracket(')')), PFactParams.b_item_b),
    (GrammarRule(POpenBracket('('), PExpressionList, PCloseBracket(')')), PFactParams.b_itemlist_b),

    # Associative Pair
    (GrammarRule(PValue, PManageOperation(':'), PValue), PAssociativePair.item_o_item),
    (GrammarRule(PValue, PManageOperation(':'), PParams), PAssociativePair.item_o_item),
    (GrammarRule(PParams, PManageOperation(':'), PValue), PAssociativePair.item_o_item),
    (GrammarRule(PParams, PManageOperation(':'), PParams), PAssociativePair.item_o_item),
    (GrammarRule(PValue, PManageOperation(':'), PType, PValue), PAssociativePair.item_o_type_item),
    (GrammarRule(PParams, PManageOperation(':'), PType, PValue), PAssociativePair.item_o_type_item),

    # Expression
    (GrammarRule(PValue, PImmutableOperation, PValue), PExpression.item_operation_item),
    (GrammarRule(PParams, PImmutableOperation, PValue), PExpression.item_operation_item),
    (GrammarRule(PValue, PImmutableOperation, PParams), PExpression.item_operation_item),
    (GrammarRule(PParams, PImmutableOperation, PParams), PExpression.item_operation_item),


    # COMPLEX TYPES

    # Assign reference value
    (GrammarRule(PLValue, PAssignOperation, PRValue), PInitVar.lvalue_o_value),
    (GrammarRule(PLValue, PAssignOperation, PType, PValue), PInitVar.lvalue_o_type_value),

    # Define function
    (GrammarRule(PName, PFormalParams, PAssignOperation, PContext), PInitFunc.lvalue_params_o_context),
    (GrammarRule(PName, PFormalParams, PAssignOperation, PFuncType, PContext), PInitFunc.lvalue_params_o_type_context),
    (GrammarRule(PCaller, PAssignOperation, PContext), PInitFunc.caller_o_context),
    (GrammarRule(PCaller, PAssignOperation, PFuncType, PContext), PInitFunc.caller_o_type_context),

    # Define type
    (GrammarRule(PType, PAssignOperation, PStrctObject), PInitType.lvalue_o_value),
    (GrammarRule(PType, PAssignOperation, PFuncType, PStrctObject), PInitType.lvalue_o_type_value),

    # Caller
    (GrammarRule(PType, PParams), PCaller.type_params),
    (GrammarRule(PValue, PParams), PCaller.value_params),

    # LISTS OF ELEMENTS

    # AssociativePair List
    (GrammarRule(PAssociativePairList, POperator(','), PAssociativePair), PAssociativePairList.list_o_item),
    (GrammarRule(PAssociativePair, POperator(','), PAssociativePair), PAssociativePairList.item_o_item),

    # Name List
    (GrammarRule(PNameList, POperator(','), PName), PNameList.list_o_item),
    (GrammarRule(PName, POperator(','), PName), PNameList.item_o_item),

    # Type List
    (GrammarRule(PTypeList, POperator(','), PType), PTypeList.list_o_item),
    (GrammarRule(PType, POperator(','), PType), PTypeList.item_o_item),

    # Expression List
    (GrammarRule(PNameList, POperator(','), PValue), PExpressionList.list_o_item),
    (GrammarRule(PValue, POperator(','), PNameList), PExpressionList.item_o_list),
    (GrammarRule(PExpressionList, POperator(','), PValue), PExpressionList.list_o_item),
    (GrammarRule(PValue, POperator(','), PValue), PExpressionList.item_o_item),
    (GrammarRule(PNameList, POperator(','), PParams), PExpressionList.list_o_item),
    (GrammarRule(PParams, POperator(','), PNameList), PExpressionList.item_o_list),
    (GrammarRule(PExpressionList, POperator(','), PParams), PExpressionList.list_o_item),
    (GrammarRule(PParams, POperator(','), PValue), PExpressionList.item_o_item),

    # Instruction List
    (GrammarRule(PInstruction, PInstruction), PInstructionList.item_item),
    (GrammarRule(PInstructionList, PInstruction), PInstructionList.item_list),

    # Define List
    (GrammarRule(PInitList, POperator(','), PInit), PInitList.list_o_item),
    (GrammarRule(PInit, POperator(','), PInit), PInitList.item_o_item),

    # LAST OF ALL Instruction
    (GrammarRule(BaseParserType, POperator(';')), PInstruction.bo)
]
