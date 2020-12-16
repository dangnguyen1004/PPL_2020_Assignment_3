from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program(self.visit(ctx.var_declars_part()) + self.visit(ctx.func_declars_part()))
    def visitVar_declars_part(self,ctx:BKITParser.Var_declars_partContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.var_declar()) + self.visit(ctx.var_declars_part())
        else:
            return []

    def visitVar_declar(self,ctx:BKITParser.Var_declarContext):
        return self.visit(ctx.var_list())

    def visitVar_list(self,ctx:BKITParser.Var_listContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.variable()) + self.visit(ctx.var_list())
        else:
            return self.visit(ctx.variable())   

    def visitVariable(self,ctx:BKITParser.VariableContext):
        return [self.visit(ctx.getChild(0))]

    def visitScalar(self,ctx:BKITParser.ScalarContext):
        if ctx.getChildCount() == 3:
            return VarDecl(Id(ctx.ID().getText()),[],self.visit(ctx.init_value()))
        else:
            return VarDecl(Id(ctx.ID().getText()),[],None)

    def visitComposite(self,ctx:BKITParser.CompositeContext):
        if ctx.getChildCount() == 4:

            return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.dimensions_of_var()),self.visit(ctx.init_value()))
        else:
            return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.dimensions_of_var()),None)

    def visitDimensions_of_var(self,ctx:BKITParser.Dimensions_of_varContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.dimen_of_var())] + self.visit(ctx.dimensions_of_var())
        else:
            return [self.visit(ctx.dimen_of_var())]

    def visitDimen_of_var(self,ctx:BKITParser.Dimen_of_varContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.int_lit_dimen())
        else:
            return None

    def visitInt_lit_dimen(self,ctx:BKITParser.Int_lit_dimenContext):
        if ctx.INT_DECE():
            return int(ctx.INT_DECE().getText())
        elif ctx.INT_HEXA():
            return int(ctx.INT_HEXA().getText(),16)
        else:
            return int(ctx.INT_OCTO().getText(),8)

    def visitDimensions(self,ctx:BKITParser.DimensionsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.dimen())] + self.visit(ctx.dimensions())
        else:
            return [self.visit(ctx.dimen())]

    def visitDimen(self,ctx:BKITParser.DimenContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.relation())
        else:
            return None

    def visitInit_value(self,ctx:BKITParser.Init_valueContext):
        return self.visit(ctx.getChild(0))

    def visitFunc_declars_part(self,ctx:BKITParser.Func_declars_partContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.func_declar())] + self.visit(ctx.func_declars_part())
        else:
            return []        

    def visitFunc_declar(self,ctx:BKITParser.Func_declarContext):
        return FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.para_declar()),self.visit(ctx.body_declar()))

    def visitPara_declar(self,ctx:BKITParser.Para_declarContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.list_para())
        else:
            return []
    def visitList_para(self,ctx:BKITParser.List_paraContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.para())] + self.visit(ctx.list_para())
        else:
            return [self.visit(ctx.para())]

    def visitPara(self,ctx:BKITParser.ParaContext):
        return self.visit(ctx.getChild(0))

    def visitScalar_para(self,ctx:BKITParser.Scalar_paraContext):
        return VarDecl(Id(ctx.ID().getText()),[],None)

    def visitComposite_para(self,ctx:BKITParser.Composite_paraContext):
        return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.dimensions_of_var()),None)

    def visitBody_declar(self,ctx:BKITParser.Body_declarContext):
        return self.visit(ctx.list_stmts())

    def visitList_stmts(self,ctx:BKITParser.List_stmtsContext):
        return (self.visit(ctx.list_var_stmts()),self.visit(ctx.list_other_stmts()))

    def visitList_var_stmts(self,ctx:BKITParser.List_var_stmtsContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.var_declar()) + self.visit(ctx.list_var_stmts())
        else:
            return []

    def visitList_other_stmts(self,ctx:BKITParser.List_other_stmtsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.stmt())] + self.visit(ctx.list_other_stmts())
        else:
            return []

    def visitStmt(self,ctx:BKITParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssign_stmt(self,ctx:BKITParser.Assign_stmtContext):
        if ctx.ID():
            return Assign(Id(ctx.ID().getText()),self.visit(ctx.getChild(2)))
        else:
            return Assign(self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
            
    def visitIf_stmt(self,ctx:BKITParser.If_stmtContext):
        ifthenstmt = [(self.visit(ctx.relation()),self.visit(ctx.list_var_stmts()),self.visit(ctx.list_other_stmts()))] + self.visit(ctx.list_elseif())
        elsestmt = self.visit(ctx.case_else())
        return If(ifthenstmt,elsestmt)

    def visitList_elseif(self,ctx:BKITParser.List_elseifContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.el_if())] + self.visit(ctx.list_elseif())
        else:
            return []

    def visitEl_if(self,ctx:BKITParser.El_ifContext):
        return (self.visit(ctx.relation()),self.visit(ctx.list_var_stmts()),self.visit(ctx.list_other_stmts()))

    def visitCase_else(self,ctx:BKITParser.Case_elseContext):
        if ctx.getChildCount() == 3:
            return (self.visit(ctx.list_var_stmts()),self.visit(ctx.list_other_stmts()))
        else:
            return ([],[])

    def visitFor_stmt(self,ctx:BKITParser.For_stmtContext):
        return For(Id(ctx.ID().getText()),self.visit(ctx.getChild(4)),self.visit(ctx.getChild(6)),self.visit(ctx.getChild(8)),self.visit(ctx.list_stmts()))

    def visitWhile_stmt(self,ctx:BKITParser.While_stmtContext):
        return While(self.visit(ctx.relation()),self.visit(ctx.list_stmts()))

    def visitDo_stmt(self,ctx:BKITParser.Do_stmtContext):
        return Dowhile(self.visit(ctx.list_stmts()),self.visit(ctx.relation()))

    def visitBreak_stmt(self,ctx:BKITParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self,ctx:BKITParser.Continue_stmtContext):
        return Continue()

    def visitCall_stmt(self,ctx:BKITParser.Call_stmtContext):
        return CallStmt(Id(ctx.ID().getText()),self.visit(ctx.list_args()))

    def visitCall(self,ctx:BKITParser.CallContext):
        return CallExpr(Id(ctx.ID().getText()),self.visit(ctx.list_args()))

    def visitList_args(self,ctx:BKITParser.List_argsContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.relation())] + self.visit(ctx.list_args())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.relation())]
        else:
            return []

    def visitReturn_stmt(self,ctx:BKITParser.Return_stmtContext):
        if ctx.getChildCount() == 3:
            return Return(self.visit(ctx.relation()))
        else:
            return Return(None)
        
    def visitRelation(self,ctx:BKITParser.RelationContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.getChild(1)),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))

    def visitLogical(self,ctx:BKITParser.LogicalContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.getChild(1)),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.exp())

    def visitLogical_op(self,ctx:BKITParser.Logical_opContext):
        return ctx.getChild(0).getText()

    def visitRelation_op(self,ctx:BKITParser.RelationContext):
        return ctx.getChild(0).getText()

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.exp2())

    def visitExp2(self,ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(),self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self,ctx:BKITParser.Exp3Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.exp4())
        
    def visitExp4(self,ctx:BKITParser.Exp4Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self,ctx:BKITParser.Exp5Context):
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.exp5()),self.visit(ctx.dimensions()))
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self,ctx:BKITParser.Exp6Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.getChild(1))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0))

    def visitBool_lit(self,ctx:BKITParser.Bool_litContext):
        return BooleanLiteral((ctx.getChild(0).getText()))

    def visitInt_lit(self,ctx:BKITParser.Int_litContext):
        if ctx.INT_DECE():
            return IntLiteral(int(ctx.INT_DECE().getText()))
        elif ctx.INT_HEXA():
            return IntLiteral(int(ctx.INT_HEXA().getText(),16))
        else:
            return IntLiteral(int(ctx.INT_OCTO().getText(),8))

    def visitFloat_lit(self,ctx:BKITParser.Float_litContext):
        return FloatLiteral(float(ctx.getChild(0).getText()))

    def visitString_lit(self,ctx:BKITParser.String_litContext):
        return StringLiteral(str(ctx.getChild(0).getText()))

    def visitArray_lit(self,ctx:BKITParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.getChild(1)))

    def visitArray_lit_element(self,ctx:BKITParser.Array_lit_elementContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.init_value())] + self.visit(ctx.array_lit_element())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.init_value())]
        else:
            return []

    def visitBuiltin_func(self,ctx:BKITParser.Builtin_funcContext):
        return self.visit(ctx.getChild(0))
    
    def visitPrint_ln(self,ctx:BKITParser.Print_lnContext):
        return CallStmt(ctx.getChild(0).getText(),[])

    def visitPrint_func(self,ctx:BKITParser.Print_funcContext):
        return CallStmt(ctx.getChild(0),[self.visit(ctx.ralation())])
    
    def visitPrint_str_ln(self,ctx:BKITParser.Print_str_lnContext):
        return CallStmt(ctx.getChild(0).getText(),[self.visit(ctx.relation())])
    
    def visitRead(self,ctx:BKITParser.ReadContext):
        return CallStmt(ctx.READ().getText(),[])

    

