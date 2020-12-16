# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declars_part.
    def visitVar_declars_part(self, ctx:BKITParser.Var_declars_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declar.
    def visitVar_declar(self, ctx:BKITParser.Var_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar.
    def visitScalar(self, ctx:BKITParser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite.
    def visitComposite(self, ctx:BKITParser.CompositeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimensions_of_var.
    def visitDimensions_of_var(self, ctx:BKITParser.Dimensions_of_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimen_of_var.
    def visitDimen_of_var(self, ctx:BKITParser.Dimen_of_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_lit_dimen.
    def visitInt_lit_dimen(self, ctx:BKITParser.Int_lit_dimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimensions.
    def visitDimensions(self, ctx:BKITParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimen.
    def visitDimen(self, ctx:BKITParser.DimenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_value.
    def visitInit_value(self, ctx:BKITParser.Init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declars_part.
    def visitFunc_declars_part(self, ctx:BKITParser.Func_declars_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declar.
    def visitFunc_declar(self, ctx:BKITParser.Func_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_declar.
    def visitPara_declar(self, ctx:BKITParser.Para_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_para.
    def visitList_para(self, ctx:BKITParser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para.
    def visitPara(self, ctx:BKITParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar_para.
    def visitScalar_para(self, ctx:BKITParser.Scalar_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_para.
    def visitComposite_para(self, ctx:BKITParser.Composite_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body_declar.
    def visitBody_declar(self, ctx:BKITParser.Body_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_stmts.
    def visitList_stmts(self, ctx:BKITParser.List_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_var_stmts.
    def visitList_var_stmts(self, ctx:BKITParser.List_var_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_other_stmts.
    def visitList_other_stmts(self, ctx:BKITParser.List_other_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stmt.
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_elseif.
    def visitList_elseif(self, ctx:BKITParser.List_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#el_if.
    def visitEl_if(self, ctx:BKITParser.El_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#case_else.
    def visitCase_else(self, ctx:BKITParser.Case_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stmt.
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_stmt.
    def visitDo_stmt(self, ctx:BKITParser.Do_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stmt.
    def visitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call.
    def visitCall(self, ctx:BKITParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_args.
    def visitList_args(self, ctx:BKITParser.List_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#builtin_func.
    def visitBuiltin_func(self, ctx:BKITParser.Builtin_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#print_ln.
    def visitPrint_ln(self, ctx:BKITParser.Print_lnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#print_func.
    def visitPrint_func(self, ctx:BKITParser.Print_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#print_str_ln.
    def visitPrint_str_ln(self, ctx:BKITParser.Print_str_lnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#read.
    def visitRead(self, ctx:BKITParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relation.
    def visitRelation(self, ctx:BKITParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relation_op.
    def visitRelation_op(self, ctx:BKITParser.Relation_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical.
    def visitLogical(self, ctx:BKITParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_op.
    def visitLogical_op(self, ctx:BKITParser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_lit.
    def visitBool_lit(self, ctx:BKITParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_lit.
    def visitInt_lit(self, ctx:BKITParser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_lit.
    def visitFloat_lit(self, ctx:BKITParser.Float_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_lit.
    def visitString_lit(self, ctx:BKITParser.String_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit_element.
    def visitArray_lit_element(self, ctx:BKITParser.Array_lit_elementContext):
        return self.visitChildren(ctx)



del BKITParser