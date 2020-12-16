
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass
class Un(Type):
    pass
@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

def printEnvironments(listEnvironments):
    for environment in listEnvironments:
        for var in environment:
            print(var)
        print("")

def findFirstDuplicateParam(listParam):
    param_set = set()
    no_duplicate = 'NotDuplicate'
    for i in range(len(listParam)):
        if listParam[i] in param_set:
            return listParam[i]
        else:
            param_set.add(listParam[i])
    return no_duplicate

def assignTypeTo(exp, typ, c, listUnknownFunction):
    # Find exp in environments
    symbol = None
    if type(exp) is ArrayCell:
        exp = exp.arr
    if type(exp) is CallExpr:
        exp = exp.method
    declFound = False
    for environment in c:
        for decl in environment:
            if decl.name == exp.name: 
                symbol = decl
                declFound = True
                break 
        if declFound: break
    if not(declFound):
        for decl in listUnknownFunction:
            if decl.name == exp.name:
                symbol = decl
    # Assign type to exp
    if type(symbol.mtype) is ArrayType:
        symbol.mtype.eletype = typ
    elif type(symbol.mtype) is MType:
        symbol.mtype.restype = typ
    else:
        symbol.mtype = typ

class StaticChecker(BaseVisitor):
    listUnknownFunction: List[Symbol]
    isAfterMain: bool
    isSecondTime: bool
    def __init__(self,ast):
        self.listUnknownFunction = []
        self.isAfterMain = False
        self.isSecondTime = False
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        # decl : List[Decl]
        # Visit VarDecl first
        environment = [c]
        [self.visit(decl, environment) for decl in ast.decl if type(decl) is VarDecl]
        # Prototype funcdecl
        listDeclName = [] + [decl.name for decl in c]
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                # check redeclared param
                listParamName = [param.variable.name for param in decl.param]
                if findFirstDuplicateParam(listParamName) != 'NotDuplicate': 
                    raise Redeclared(Parameter(), findFirstDuplicateParam(listParamName))
                listInputType = [Unknown() for i in range(0,len(decl.param))]
                typeOfReturn = Unknown()
                isHaveReturn = False
                for stmt in decl.body[1]:
                    if type(stmt) is Return:
                        if stmt.expr is not None:
                            isHaveReturn = True
                            break
                if not(isHaveReturn): typeOfReturn = VoidType()
                environment[0] += [Symbol(decl.name.name, MType(listInputType, typeOfReturn))]
                if decl.name.name in listDeclName: raise Redeclared(Function(), decl.name.name)
                else: listDeclName += [decl.name.name]
            else: listDeclName += [decl.variable.name]
        # Visit FuncDecl
        [self.visit(decl, environment) for decl in ast.decl if type(decl) is FuncDecl]
        # Check no entry point
        haveEntryPoint = False
        for decl in environment[0]:
            if type(decl.mtype) is MType and decl.name == 'main':
                haveEntryPoint = True
                break
        if not(haveEntryPoint): raise NoEntryPoint()

    def visitVarDecl(self,ast, c):
        # variable : Id
        # varDimen : List[int] # empty list for scalar variable
        # varInit  : Literal   # null if no initial
        name = ast.variable.name
        for declInCurrentEnvironment in c[0]:
            if declInCurrentEnvironment.name == name: 
                raise Redeclared(Variable(), name)
        
        if (ast.varInit):
            typeOfInit = self.visit(ast.varInit, c)
            c[0] += [Symbol(name, typeOfInit)]
        elif ast.varDimen != []:
            c[0] += [Symbol(name, ArrayType(ast.varDimen, Unknown()))]
        else:
            c[0] += [Symbol(name, Unknown())]

    def visitFuncDecl(self,ast, c):
        # name: Id
        # param: List[VarDecl]
        # body: Tuple[List[VarDecl],List[Stmt]]
        name = ast.name.name
        # Find declarion in environment
        for decl in c[0]: 
            if decl.name == name:
                functionDeclared = decl
        # Visit VarDecl
        listParam = [[]]
        [self.visit(param, listParam) for param in ast.param]
        listParamName = [param.name for param in listParam[0]]
        # Assign param type 
        for index in range(0, len(listParam[0])):
            if type(listParam[0][index].mtype) is ArrayType:
                listParam[0][index].mtype.eletype = functionDeclared.mtype.intype[index]
            else:
                listParam[0][index].mtype = functionDeclared.mtype.intype[index]
        # Visit Local Var
        listLocalVar = [listParam[0]]
        [self.visit(localVar, listLocalVar) for localVar in ast.body[0]]
        # Visit stmts:
        newEnvironment = listLocalVar + c
        typeOfReturn = None
        for stmt in ast.body[1]:
            if type(stmt) is Return:
                typeOfReturn = self.visit(stmt, newEnvironment)
                if type(typeOfReturn) is Unknown:
                    raise TypeCannotBeInferred(stmt)
                if type(functionDeclared.mtype.restype) is not Unknown and type(functionDeclared.mtype.restype) != type(typeOfReturn):
                    raise TypeMismatchInStatement(stmt)
            else:
                self.visit(stmt, newEnvironment)
        # Assign type back
        listParam = [decl for decl in newEnvironment[0] if decl.name in listParamName]
        listParamType = [param.mtype for param in listParam]
        functionDeclared.mtype.intype = listParamType
        # Return type
        if typeOfReturn is None:
            functionDeclared.mtype.restype = VoidType()
        else: functionDeclared.mtype.restype = typeOfReturn
    def visitReturn(self,ast, c):
        # expr:Expr # None if no expression
        if ast.expr is not None: return self.visit(ast.expr, c)
        else: return VoidType()

    def visitId(self,ast, c):
        # name : str
        for environment in c:
            for decl in environment:
                if decl.name == ast.name: return decl.mtype  
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self,ast, c):
        # arr:Expr
        # idx:List[Expr]
        typeOfArr = self.visit(ast.arr, c)
        if type(typeOfArr) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        # Check type of list idx
        listTypeOfIdx = [self.visit(idx, c) for idx in ast.idx]
        for typeOfIdx in listTypeOfIdx:
            if type(typeOfIdx) is not IntType:
                raise TypeMismatchInExpression(ast)
        # Check number of dimen
        if (len(typeOfArr.dimen) != len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        # Return
        return typeOfArr.eletype

    def visitCallExpr(self,ast, c):
        # method:Id
        # param:List[Expr]
        name = ast.method.name
        functionCall = None
        for decl in c[len(c) - 1]:
            if decl.name == name and type(decl.mtype) is MType:
                functionCall = decl
                break
        if functionCall is None: raise Undeclared(Function(), name)
        listTypeOfParam = [self.visit(param, c) for param in ast.param]
        if len(listTypeOfParam) != len(functionCall.mtype.intype):
            raise TypeMismatchInExpression(ast)
        for index in range(0, len(listTypeOfParam)):
            typeOfArg = functionCall.mtype.intype[index]
            typeOfParam = listTypeOfParam[index]
            if type(typeOfArg) is Unknown and type(typeOfParam) is Unknown:
                return Un()
            elif type(typeOfArg) is Unknown:
                functionCall.mtype.intype[index] = typeOfParam
            elif type(typeOfParam) is Unknown:
                assignTypeTo(ast.param[index], typeOfArg, c, self.listUnknownFunction)
            elif type(typeOfArg) != type(typeOfParam):
                raise TypeMismatchInExpression(ast)
        return functionCall.mtype.restype

    def visitAssign(self,ast, c):
        # lhs: LHS
        # rhs: Expr
        typeOfRhs = self.visit(ast.rhs, c)
        typeOfLhs = self.visit(ast.lhs, c)
        if type(typeOfLhs) is Unknown and type(typeOfRhs) is Unknown:
            raise TypeCannotBeInferred(ast)
        if type(typeOfLhs) is Unknown and type(typeOfRhs) is Un:
            raise TypeCannotBeInferred(ast)
        if type(typeOfLhs) is Un and type(typeOfRhs) is Unknown:
            raise TypeCannotBeInferred(ast)
        if type(typeOfLhs) is Un and type(typeOfRhs) is Un:
            raise TypeCannotBeInferred(ast)
        elif type(typeOfLhs) is Unknown:
            assignTypeTo(ast.lhs, typeOfRhs, c, self.listUnknownFunction)
        elif type(typeOfLhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(typeOfRhs) is Unknown:
            assignTypeTo(ast.rhs, typeOfLhs, c, self.listUnknownFunction)
        elif type(typeOfRhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(typeOfLhs) != type(typeOfRhs):
            raise TypeMismatchInStatement(ast)

    def visitIf(self,ast, c):
        # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        for ifThenStmt in ast.ifthenStmt:
            conditionExp = self.visit(ifThenStmt[0], c)
            if type(conditionExp) is Unknown:
                assignTypeTo(ifThenStmt[0], BoolType(), c, self.listUnknownFunction)
            elif type(conditionExp) is not BoolType:
                raise TypeMismatchInStatement(ast)
            listLocalVar = [[]]
            [self.visit(localVar, listLocalVar) for localVar in ifThenStmt[1]]
            newEnvironment = listLocalVar + c
            [self.visit(stmt, newEnvironment) for stmt in ifThenStmt[2]]
        # else
        listLocalVar = [[]]
        [self.visit(localVar, listLocalVar) for localVar in ast.elseStmt[0]]
        newEnvironment = listLocalVar + c
        [self.visit(stmt, newEnvironment) for stmt in ast.elseStmt[1]]

    def visitFor(self,ast, c):
        # idx1: Id
        # expr1:Expr
        # expr2:Expr
        # expr3:Expr
        # loop: Tuple[List[VarDecl],List[Stmt]]
        idx = self.visit(ast.idx1, c)
        exp1 = self.visit(ast.expr1, c)
        exp2 = self.visit(ast.expr2, c)
        exp3 = self.visit(ast.expr3, c)
        if type(exp1) is Unknown:
            assignTypeTo(ast.expr1, IntType(), c, self.listUnknownFunction)
        elif type(exp1) is not IntType:
            raise TypeMismatchInStatement(ast)
        if type(idx) is Unknown:
            assignTypeTo(ast.idx1, IntType(), c, self.listUnknownFunction)
        elif type(idx) is not IntType:
            raise TypeMismatchInStatement(ast)
        if type(exp3) is Unknown:
            assignTypeTo(ast.expr3, IntType(), c, self.listUnknownFunction)
        elif type(exp3) is not IntType:
            raise TypeMismatchInStatement(ast)
        if type(exp2) is Unknown:
            assignTypeTo(ast.expr2, BoolType(), c, self.listUnknownFunction)
        elif type(exp2) is not BoolType:
            raise TypeMismatchInStatement(ast)
        listLocalVar = [[]]
        [self.visit(localVar, listLocalVar) for localVar in ast.loop[0]]
        newEnvironment = listLocalVar + c
        [self.visit(stmt, newEnvironment) for stmt in ast.loop[1]]

    def visitDowhile(self,ast, c):
        # sl:Tuple[List[VarDecl],List[Stmt]]
        # exp: Expr
        exp = self.visit(ast.exp, c)
        if type(exp) is Unknown:
            assignTypeTo(ast.exp, BoolType(), c, self.listUnknownFunction)
        elif type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        listLocalVar = [[]]
        [self.visit(localVar, listLocalVar) for localVar in ast.sl[0]]
        newEnvironment = listLocalVar + c
        [self.visit(stmt, newEnvironment) for stmt in ast.sl[1]]

    def visitWhile(self,ast, c):
        # exp: Expr
        # sl:Tuple[List[VarDecl],List[Stmt]]
        exp = self.visit(ast.exp, c)
        if type(exp) is Unknown:
            assignTypeTo(ast.exp, BoolType(), c, self.listUnknownFunction)
        elif type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        listLocalVar = [[]]
        [self.visit(localVar, listLocalVar) for localVar in ast.sl[0]]
        newEnvironment = listLocalVar + c
        [self.visit(stmt, newEnvironment) for stmt in ast.sl[1]]            

    def visitCallStmt(self,ast, c):
        # method:Id
        # param:List[Expr]
        name = ast.method.name
        functionCall = None
        for environment in c:
            for decl in environment:
                if decl.name == name and type(decl.mtype) is MType:
                    functionCall = decl
                    break
        if functionCall is None: raise Undeclared(Function(), name)
        listTypeOfParam = [self.visit(param, c) for param in ast.param]
        if type(functionCall.mtype.restype) is Unknown:
            functionCall.mtype.restype = VoidType()
        if type(functionCall.mtype.restype) is not VoidType: 
            raise TypeMismatchInStatement(ast)
        if len(listTypeOfParam) != len(functionCall.mtype.intype):
            raise TypeMismatchInStatement(ast)
        for index in range(0, len(listTypeOfParam)):
            typeOfArg = functionCall.mtype.intype[index]
            typeOfParam = listTypeOfParam[index]
            if type(typeOfArg) is Unknown and type(typeOfParam) is Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(typeOfArg) is Unknown:
                functionCall.mtype.intype[index] = typeOfParam
            elif type(typeOfParam) is Unknown:
                assignTypeTo(ast.param[index], typeOfArg, c, self.listUnknownFunction)
            elif type(typeOfArg) != type(typeOfParam):
                raise TypeMismatchInStatement(ast)
    def visitBinaryOp(self,ast, c):
        # op:str
        # left:Expr
        # right:Expr
        operator = ast.op
        typeOfLeft = self.visit(ast.left, c)
        typeOfRight = self.visit(ast.right, c)

        if operator in ['+','-','*','\\','%']:
            if type(typeOfLeft) is IntType and type(typeOfRight) is IntType:
                return IntType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is IntType:
                assignTypeTo(ast.left, IntType(), c, self.listUnknownFunction)
                return IntType()
            elif type(typeOfLeft) is IntType and type(typeOfRight) is Unknown:
                assignTypeTo(ast.right, IntType(), c, self.listUnknownFunction)
                return IntType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is Unknown:
                assignTypeTo(ast.left, IntType(), c, self.listUnknownFunction)
                assignTypeTo(ast.right, IntType(), c, self.listUnknownFunction)
                return IntType()
            elif type(typeOfLeft) is Un or type(typeOfRight) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        elif operator in ['>','<','>=','<=','==','!=']:
            if type(typeOfLeft) is IntType and type(typeOfRight) is IntType:
                return BoolType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is IntType:
                assignTypeTo(ast.left, IntType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is IntType and type(typeOfRight) is Unknown:
                assignTypeTo(ast.right, IntType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is Unknown:
                assignTypeTo(ast.left, IntType(), c, self.listUnknownFunction)
                assignTypeTo(ast.right, IntType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is Un or type(typeOfRight) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        elif operator in ['+.','-.','*.','\\.']:
            if type(typeOfLeft) is FloatType and type(typeOfRight) is FloatType:
                return FloatType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is FloatType:
                assignTypeTo(ast.left, FloatType(), c, self.listUnknownFunction)
                return FloatType()
            elif type(typeOfLeft) is FloatType and type(typeOfRight) is Unknown:
                assignTypeTo(ast.right, FloatType(), c, self.listUnknownFunction)
                return FloatType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is Unknown:
                assignTypeTo(ast.left, FloatType(), c, self.listUnknownFunction)
                assignTypeTo(ast.right, FloatType(), c, self.listUnknownFunction)
                return FloatType()
            elif type(typeOfLeft) is Un or type(typeOfRight) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        elif operator in ['=/=','<.','>.','<=.','>=.']:
            if type(typeOfLeft) is FloatType and type(typeOfRight) is FloatType:
                return BoolType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is FloatType:
                assignTypeTo(ast.left, FloatType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is FloatType and type(typeOfRight) is Unknown:
                assignTypeTo(ast.right, FloatType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is Unknown:
                assignTypeTo(ast.left, FloatType(), c, self.listUnknownFunction)
                assignTypeTo(ast.right, FloatType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is Un or type(typeOfRight) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        elif operator in ['&&','||']:
            if type(typeOfLeft) is BoolType and type(typeOfRight) is BoolType:
                return BoolType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is BoolType:
                assignTypeTo(ast.left, BoolType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is BoolType and type(typeOfRight) is Unknown:
                assignTypeTo(ast.right, BoolType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is Unknown and type(typeOfRight) is Unknown:
                assignTypeTo(ast.left, BoolType(), c, self.listUnknownFunction)
                assignTypeTo(ast.right, BoolType(), c, self.listUnknownFunction)
                return BoolType()
            elif type(typeOfLeft) is Un or type(typeOfRight) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast, c):
        # op:str
        # body:Expr 
        operator = ast.op
        typeOfExp = self.visit(ast.body, c)

        if operator == '!':
            if type(typeOfExp) is BoolType:
                return BoolType()
            elif type(typeOfExp) is Unknown:
                assignTypeTo(typeOfExp, BoolType(), c, self.listUnknownFunction)
                return BoolType(0)
            elif type(typeOfExp) is Un:
                 return Un()
            else: 
                raise TypeMismatchInExpression(ast)
        elif operator == '-':
            if type(typeOfExp) is IntType:
                return IntType()
            elif type(typeOfExp) is Unknown:
                assignTypeTo(typeOfExp, IntType(), c, self.listUnknownFunction)
                return IntType()
            elif type(typeOfExp) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        elif operator == '-.':
            if type(typeOfExp) is FloatType:
                return FloatType()
            elif type(typeOfExp) is Unknown:
                assignTypeTo(typeOfExp, FloatType(), c, self.listUnknownFunction)
                return FloatType()
            elif type(typeOfExp) is Un:
                 return Un()
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self,ast, c):
        return FloatType()

    def visitStringLiteral(self,ast, c):
        return StringType()
        
    def visitBooleanLiteral(self,ast, c):
        return BoolType()

    def visitArrayLiteral(self,ast, c):
        # value:List[Literal]
        if len(ast.value) > 0:
            typeOfFirstElement = self.visit(ast.value[0], c)
            if type(typeOfFirstElement) is ArrayType:
                return ArrayType([len(ast.value)] + typeOfFirstElement.dimen, typeOfFirstElement.eletype)
            else:
                return ArrayType([len(ast.value)], typeOfFirstElement)
        else: 
            return ArrayType([],Unknown())







        
