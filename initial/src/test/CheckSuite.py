import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_case_1(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_case_2(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_case_3(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_case_4(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_case_5(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_case_6(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_case_7(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: m,n,p
                  Body:
                        m = 1;
                        n = "string";
                        p = string_of_int(m);
                        Return p;
                  EndBody.

                  Function: main
                  Parameter: x,y,z
                  Body:
                       foo(fact(100,"a","b"), 1);
                  EndBody.

                  Function: foo
                  Parameter: x,y
                  Body:
                       y = 0x9; 
                       x = 1;
                  EndBody.

                  """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_case_8(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            If x Then
                While x Do
                    If x Then
                        Break;
                    ElseIf False Then
                        Continue;
                    EndIf.
                EndWhile.
            Else
            EndIf.
        EndBody.
        """
        expect =  str()
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_case_9(self):
        """More complex program"""
        input = """
                  Function: fact
                  Parameter: m,n,p
                  Body:
                        m = 1;
                        n = "string";
                        p = string_of_int(m);
                        Return { { 1.1, 1.2 } , { 1.3, 1.4 }, { 1.5, 1.6 } };
                  EndBody.

                  Function: main
                  Parameter: x,y,z
                  Body:
                       foo(fact(100,"a","b")[2][1], 1);
                  EndBody.

                  Function: foo
                  Parameter: x,y
                  Body:
                       y = 0x9; 
                       x = 1.1 +. 1.2;
                       Return y;
                  EndBody.

                  """
        expect = str(TypeMismatchInStatement(Return(Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_case_10(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            x = x + test(x, 1);
        EndBody.
        Function: test
        Parameter: x, y
        Body:
            Return x + y;
        EndBody.
        """
        expect =  str()
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_case_11(self):
        input = """
        Var: x, a, b;
        Function: main
        Parameter: x
        Body:
            Var: k;
            k = foo(4 * a - b, x && False) && k;
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
            test();
            Return x;
        EndBody.
        Function: test
        Body:
            x = test();
        EndBody.
        """
        expect =  str(TypeMismatchInStatement(Assign(Id('x'),CallExpr(Id('test'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_case_12(self):
        input = """
                    Var: x[2][3], y, z[1][3];
                    Function: main
                    Body:
                        x[1] = x[1 + foo("3",-9)] + 10;
                    EndBody.
                """
        expect = str(TypeMismatchInExpression(BinaryOp(
                                "+",
                                ArrayCell(
                                    Id("x"),
                                    [
                                        BinaryOp(
                                            "+",
                                            IntLiteral(1),
                                            CallExpr(
                                                Id("foo"),
                                                [
                                                    StringLiteral("3"),
                                                    UnaryOp("-", IntLiteral(9))
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                IntLiteral(10)
                            )))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_case_13(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallStmt(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_case_14(self):
        input = """
        Var: x, a[10], b[5];
        Function: main
        Parameter: x
        Body:
            While f(2, 3)[4] Do
            EndWhile.
        EndBody.
        Function: test
        Parameter: x, y
        Body:
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: f
        Parameter: z, t
        Body:
            Return a;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(While(ArrayCell(CallExpr(Id('f'),[IntLiteral(2),IntLiteral(3)]),[IntLiteral(4)]),([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_case_15(self):
        input = """
                    Function: foo

            Parameter: x, y

            Body:

                Var: z;

                While (True) Do

                    z = foo(1, foo(x, True));

                EndWhile.

                Return y && z;

            EndBody.
                """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_case_16(self):
        """Simple program: main"""
        input = """Var: a[2][2] = {{1,2},{3,4}};"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_case_17(self):
        input = """ Var: main;
                    Function: main
                    Body: 
                    EndBody."""
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_case_18(self):
        input = """
        Var: x[10][10];
        Function: main
        Parameter: flag
        Body:
            f("s")[2][3] = 100;
            If f("a")[0][1] == foo()[1][2] Then
                f(flag)[1][3] = 0o10;
            EndIf.
            flag = 12;
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return foo();
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('f'),[StringLiteral("""s""")]),[IntLiteral(2),IntLiteral(3)]),IntLiteral(100))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_case_19(self):
        input = """
                    Var: a;
                    Function: main
                    Body:
                        a = foo();
                    EndBody.
                    Function: foo
                    Body:
                        Return 1;
                    EndBody.
                """
        expect = str(TypeCannotBeInferred(Assign(Id("a"), CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,419))


    def test_case_20(self):
        input = """
        Var: x[10][10], m, k;
        Function: test
        Body:
            Return m + k;
        EndBody.
        Function: main
        Parameter: flag
        Body:
            test();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[])))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_case_21(self):
        input = """
        Var: x[10][10], m, k;
        Function: test
        Body:
            Return m + k + x[0][1];
        EndBody.
        Function: main
        Parameter: flag
        Body:
            flag = test();
            x[3][2] = 1.2;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'),[IntLiteral(3),IntLiteral(2)]),FloatLiteral(1.2))))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_case_22(self):
        input = """
        Var: x[10][10], m, k;
        Function: main
        Parameter: flag
        Body:
            For(flag = 1, f("a"), foo()) Do
            EndFor.
            Return flag;
        EndBody.
        Function: f
        Parameter: p
        Body:
            Return main(p) == 1;
        EndBody.
        Function: foo
        Body:
            Return x[0][1] * m + k;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('main'),[Id('p')])))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_case_23(self):
        input = """
        Var: a = 1, b = 2, c = 3; 
        Function: f
        Body:
        EndBody.
        Function: main
        Body:
            f(1,2,3.0);
        EndBody.
        
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('f'),[IntLiteral(1),IntLiteral(2),FloatLiteral(3.0)])))
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_case_24(self):
        input = """
        Var: a, b, c; 
        Function: main
        Body:
            f(1);
        EndBody.
        Function: f
        Body:
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('f'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_case_25(self):
        input = """
        Function: main
        Body:
            f();
        EndBody.
        Function: f
        Parameter: a
        Body:
            Return; 
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('f'),[])))
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_case_26(self):
        input = """
        Function: foo
        Parameter: a
        Body:
            a = 1;
            Return a;
        EndBody.
        Function: main
        Body:
            foo(2);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_case_27(self):
        input = """
        Var: a = 2;
            Function: main
            Body:
                If (a) Then
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(Id('a'),[],[])],([],[]))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_case_28(self):
        input = """
        Var: a = True;
            Function: main
            Body:
                If (a && 5) Then
                    a = False;
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('&&',Id('a'),IntLiteral(5))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_case_29(self):
        input = """
        Var: a = True;
            Function: main
            Body:
                If (False == 2 + 1) Then
                EndIf.
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('==',BooleanLiteral(False),BinaryOp('+',IntLiteral(2),IntLiteral(1)))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_case_30(self):
        input = """Var: x;
                    Function: main
                   Body: 
                        x = 1;
                        x = foo(1);
                        
                   EndBody.
                   
                   Function: foo
                   Parameter: k
                   Body:
                        k = 1.1;
                        printStrLn(k);
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("k"),FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_case_31(self):
        input = """Var: x;
                    Function: main
                   Body: 
                        x = 1;
                        x = foo(1);
                        xx();
                   EndBody.
                   Function: xx
                   Parameter: a
                   Body:
                        foo(1);
                    EndBody.
                   Function: foo
                   Parameter: k
                   Body:
                        printStrLn(k);
                   EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("xx"),[])))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_case_32(self):
        input = """
        Var: a = 1;
        Function: main
        Parameter: b
        Body:
            b = True;
            a = b;
        EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_case_33(self):
        input = """
        Var: a;
        Function: foo
        Body:
            Return 1;
        EndBody.
        Function: main
        Body:
            a = foo();
            a = "sk";
        EndBody.
        
                """
        expect = str(TypeMismatchInStatement(Assign(Id('a'),StringLiteral("sk"))))
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_case_34(self):
        input = """
        
        Var: a;
        Function: main
        Body:
            a = foo();
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        
        """
        expect = str(TypeCannotBeInferred(Assign(Id('a'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_case_35(self):
        input = """
        Var: a;
        Function: main
        Parameter: b
        Body:
            Var: b;
        EndBody.
        """
        expect = str(Redeclared(Variable(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_case_36(self):
        input = """
        Var: x[2][2] = {{1,2},{3,2}}, a;
        Function: foo
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a;
            a = foo()[1][1];
            a = 1.1;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_case_37(self):
        input = """
        Function: main
        Parameter: b, b[5][6]
        Body:
            
        EndBody.
        """
        expect = str(Redeclared(Parameter(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_case_38(self):
        input = """Function: main
                   Body: 
                        foo(1, 2);
                   EndBody.
                   Function: foo
                   Parameter: a, b
                   Body:
                        Return a;
                   EndBody."""
        expect = str(TypeMismatchInStatement(Return(Id('a'))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_case_39(self):
        input = """Function: main
                   Body: 
                        Var: x;
                        If x Then
                            x = 1;
                        EndIf.
                   EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id('x'), IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_case_40(self):
        input = """
        Function: foo
        Parameter: a
        Body:
            a = 1;
            Return a;
        EndBody.
        Function: main
        Parameter: b
        Body:
            foo();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[])))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_case_41(self):
        input = """
        Function: b
        Parameter: string_of_int
        Body: 
            Var: a ;
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Redeclared(Variable(),"string_of_int"))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_case_42(self):
        input = """
        Function: pool
        Parameter: b
        Body: 
            Var: printLn;
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Redeclared(Variable(),"printLn"))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_case_43(self):
        input = """
        Function: string_of_float
        Parameter: b
        Body: 
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Redeclared(Function(),"string_of_float"))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_case_44(self):
        input = """
        Function: id
        Parameter: b
        Body: 
            a = 10 ;
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_case_45(self):
        input = """
        Function: id
        Parameter: b
        Body: 
            foo(2);
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_case_46(self):
        input = """
        Function: id
        Parameter: b
        Body: 
            b = foo(2) + 1 ;
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_case_45(self):
        input = """
        Function: id
        Parameter: b
        Body: 
            Var: f = 10;
            b = ppl(f) ;
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Undeclared(Function(),"ppl"))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_case_46(self):
        input = """
        Function: id
        Parameter: b
        Body: 
            Var: f = 10;
            b = ass[5] ;
        EndBody.
        Function: main
        Body: 
        EndBody.
        """
        expect = str(Undeclared(Identifier(),"ass"))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_case_47(self):
        input = """
        Var: a, b;
        Function: main
        Parameter: x, y
        Body:
            reaD()[1][2][3] = 5;
        EndBody.
        """
        expect = str(Undeclared(Function(), 'reaD'))
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_case_48(self):
        input = """
        Function: a
        Parameter: b
        Body:
        EndBody.
        Function: main
        Parameter: x
        Body: 
            Var: y = 1;
            a(z);
            Return 0;
        EndBody.
        """
        expect = str(Undeclared(Identifier(),'z'))
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_case_49(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a,b
                Body:
                    If a > b Then
                        Var: i;
                        For (i = 2, i < 10, i + 1) Do
                            Var: s;
                            s = string_of_int(i);
                            print(s);
                        EndFor.
                    ElseIf a < b Then
                        Var: i = 0;
                        While i < 5 Do
                            Var: s;
                            s = string_of_int(i);
                            printStrLn(s);
                        EndWhile.
                    EndIf. 
                    Return b;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[IntLiteral(5), IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_case_50(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: a[2][2],b
                Body:
                    a[1] = 1;
                    a[1][1] = b + 2;
                    Return b;
                EndBody.
                Function: main
                Body:
                    foo(5,2);
                EndBody.
               """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('a'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_case_51(self):
        """More complex program"""
        input = """
                Function: main
                Body:
                    Var: x;
                    foo(5,x);
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                EndBody.
               """
        expect = str(TypeCannotBeInferred(CallStmt(Id('foo'),[IntLiteral(5),Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_case_52(self):
        """More complex program"""
        input = """
                Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                    foo(5,x);
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                    Return True;
                EndBody.
               """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_case_53(self):
        """More complex program"""
        input = """
                Function: foo
                Parameter: x,y
                Body:
                    x = 2;
                    y = 1;
                    Return;
                EndBody.
                Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                    foo(5.1,x);
                EndBody.
               """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[FloatLiteral(5.1), Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_case_53(self):
        """More complex program"""
        input = """
                 Function: main
                Body:
                    Var: x;
                    x = 1 + 2;
                    foo(5.1,x);
                EndBody.
                Function: foo
                Parameter: x,y
                Body:
                    x = 2;
                    y = 1;
                    Return;
                EndBody.
                
               """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_case_53(self):
        input = """ 
            Function: main
            Parameter: x, y ,z
            Body:
            y = x || (x > z);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('>',Id('x'),Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_case_54(self):
        input = """ 
        Function: foo
            Parameter: x
            Body:
            x=1.1;
            Return { True };
            EndBody.
        Function: main
            Parameter: x, y
            Body:
            foo(x)[0] = x || (x>y);
            EndBody.

        """
        expect = str(TypeMismatchInExpression(BinaryOp('||',Id('x'),BinaryOp('>',Id('x'),Id('y')))))
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_case_55(self):
        input = """ 
        Function: main
        Parameter: x, y
        Body:
            y = 1;
            foo(1.1, y);
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            y = 1;
            x = y;
        Return { True };
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),Id('y'))))
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_case_56(self):
        input = """
        Var: a, b, arr[10][10], array[10][10];
        Function: main
        Parameter: x, y, main
        Body:
            If main && x Then
                Return y + 1;
            EndIf.
            Return arr[0][0];
        EndBody.
        Function: foo
        Parameter: x, y
        Body:
            array[2][3] = x =/= y;
            arr = array;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('arr'),Id('array'))))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_case_57(self):
        input = """
        Var: a, b[2][2], c;
        Function: test
        Parameter: k
        Body:
            Do
                test(1);
            While k EndDo.
        EndBody.
        Function: main
        Body:
           b[f()][f()] = 123;
        EndBody.
        Function: f
        Body:
            Var: c[2][3];
            Return 1;
        EndBody.
        """
        expect =  str(TypeMismatchInStatement(Dowhile(([],[CallStmt(Id('test'),[IntLiteral(1)])]),Id('k'))))
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_case_58(self):
        input = """
        Var: x, y, arr[5];
        Function: foo
        Parameter: n
        Body:
            n = 10 * 2 - 1;
            Return n;
        EndBody.
        Function: main
        Body:
            Var: t, a;
            t = 10 + foo(2);
            t = factorial(t);
            arr = get_arr();
        EndBody.
        Function: factorial
        Parameter: n
        Body:
            If (n == 0) || (n == 1) Then
                Return 1;
            EndIf.
            Return n * factorial(n - 1);
        EndBody.
        Function: get_arr
        Body:
            Var: arr = {1, 2, 3, 4, 5};
            Return arr;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('arr'),CallExpr(Id('get_arr'),[]))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_case_59(self):
        input = """
        Var: x[10][10];
        Function: main
        Parameter: flag
        Body:
            Var: v;
            v = f(flag);
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return foo();
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('v'),CallExpr(Id('f'),[Id('flag')]))))
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_case_60(self):
        input = """
        Var: x[10];
        Function: main
        Parameter: flag
        Body:
            Var: s;
            s = read();
            For(flag = 0, flag < length(s), 1) Do
                x[s] = x[s] + 1;
            EndFor.
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'),[Id('s')])))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_case_61(self):
        input = """
        Var: x[10];
        Function: main
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(x);
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('length'),[Id('x')])))
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_case_62(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(flag);
            Return flag;
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        Function: main
        Body:
            Var: z;
            z = test(x[0]);
            x[0] = t;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), 't'))
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_case_63(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(flag);
            Return flag;
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        Function: foo
        Body:
            Var: z;
            z = test(x[0]);
            x[1] = z;
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_case_64(self):
        input = """
        Var: x[10];
        Function: test
        Parameter: flag
        Body:
            Var: s, x, y, t;
            s = read();
            x = length(s) * 2;
            t = length(flag);
            Return flag;
        EndBody.
        Function: length
        Parameter: s
        Body:
            Return 100;
        EndBody.
        Function: main
        Body:
            Var: z;
            z = test(x[0]);
            x[1] = z;
            printStrLn(string_of_int(length(z)));
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_case_65(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: y, z;
            x[2] = x[0o3] || (y > z);
            While x[2] && x[3] Do
                Do
                    printStrLn(string_of_int(y * z));
                    If x[0] Then
                        Return 1;
                    ElseIf x[1] Then
                        Return z;
                    Else
                        Var: k;
                        k = 10;
                    EndIf.
                    z = y;
                While x[4] EndDo.
            EndWhile.
            Return z % y;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_case_66(self):
        input = """
        Var: x[10];
        Function: foo
        Parameter: a, b
        Body:
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            t = 4;
            a[0] = t;
            a = foo(t, 4);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_case_67(self):
        input = """
        Var: x[10];
        Function: foo
        Parameter: a, b
        Body:
            b = x[5] * b % 4;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            t = 4;
            a = foo(t, 4);
            z = foo(a[2], t)[2];
            a[2] = float_of_int(z);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[IntLiteral(2)]),CallExpr(Id('float_of_int'),[Id('z')]))))
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_case_68(self):
        input = """
        Var: x[10];
        Function: foo
        Parameter: a, b
        Body:
            b = x[5] * b % 4;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            t = 4;
            foo(t, t)[2] = a[2];
            a[int_of_float(4.3 *. 2.4 \. 0.1)] = z || (t > x[1]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('a'),[CallExpr(Id('int_of_float'),[BinaryOp('\.',BinaryOp('*.',FloatLiteral(4.3),FloatLiteral(2.4)),FloatLiteral(0.1))])]),BinaryOp('||',Id('z'),BinaryOp('>',Id('t'),ArrayCell(Id('x'),[IntLiteral(1)]))))))
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_case_69(self):
        input = """
        Var: x[10];
        Function: foo
        Body:
            x[2] = 2;
            Return x;
        EndBody.
        Function: main
        Body:
            Var: a[10], t, z;
            a[9] = t * z % x[1];
            a[2] = foo()[2];
            foo()[4] = 4.3;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(4)]),FloatLiteral(4.3))))
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_case_70(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], t, z;
            a[9] = t * z;
            a = foo();
            foo()[2] = 3.4;
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2)]),FloatLiteral(3.4))))
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_case_71(self):
        """More complex program"""
        input = """
                  Var: x[2][2][3] = { { { 1,2,3 } , { 2,3,4 } } , { { 1,2,3 } , { 2,3,4 } } };
                  Function: foo
                  Parameter: z, y
                  Body:
                      Return x;
                  EndBody.

                  Function: main
                  Parameter: x[2][2][3], y
                  Body:
                      x = foo(1,2);
                      x[0][0][0] = False;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('x'), [IntLiteral(0), IntLiteral(0), IntLiteral(0)]), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_case_72(self):
        """Complex program"""
        input = """
            Function: func_name
            Parameter: k
                Body:
                    If 0==0 Then
                        Var: x;
                    ElseIf 1==1 Then
                        Var: y[1];
                    Else
                        Var: y;
                        Var: m, n[1][2][3] = "string";
                    EndIf.
                    k = 0x9;
                    For ( k=2,0<1, 1+1 ) Do
                        Var: y,m,n;
                        Var: k, n[1][2][100];
                    EndFor.
                EndBody.
                
            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Variable(), 'n'))
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_case_73(self):
        """Complex program"""
        input = """
            Function: int_of_float
            Body:
            EndBody.

            Function: main
                Body:
                EndBody.
        """
        expect = str(Redeclared(Function(), 'int_of_float'))
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_case_74(self):
        """Complex program"""
        input = """
            Function: main_
            Body:
                Var: x;
                main_();
                x = 1;
            EndBody.

            Function: main
            Body:
                Var: x;
                x = 1;
                x = 1.;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'), FloatLiteral(1.))))
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_case_75(self):
        """Complex program"""
        input = """
            Function: main_
            Body:
                Var: x;
                main_();
                x = 1;
            EndBody.

            Function: main
            Body:
                Var: x[5];
                Var: y[3] = { 1,2,  3};
                For ( i=1,i<100,1) Do
                    If 1 < 2 Then
                        x = y;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = str(Undeclared(Identifier(), 'i'))
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_case_76(self):
        """Complex program"""
        input = """
            Function: foo
            Body:
                Var: x;
                x = 1;
            EndBody.

            Function: main
            Body:
                Var: x[5];
                Var: y[3] = { 1,2,  3};
                Var: z = 1;
                z = z + foo();
                z = foo() + 0x9;
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+', Id('z'),CallExpr(Id('foo'),[]))))
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test_case_77(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y
            Body:
                Var: z;
            EndBody.

            Function: main
            Body:
                 x = foo(1);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'), [IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_case_78(self):
        """Complex program"""
        input = """
            Var: x = 1;
            Function: foo
            Parameter: x,y,   z
            Body:
                x = 1;
                y = 1.9999;
                Return y;
            EndBody.

            Function: main
            Body:
                Var: x = 1.1, y;
                 x = foo(1,1.1, "this is a string");
                 x = 1 + foo(1, 1.1, 1000);
            EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+',IntLiteral(1),CallExpr(Id('foo'), [IntLiteral(1), FloatLiteral(1.1), IntLiteral(1000)]))))
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_case_79(self):
        """Complex program"""
        input = """
            Var: a,b;
            Function: foo
            Parameter: x,y,   z
            Body:
                Return;
            EndBody.

            Function: main
            Body:
                If b + 0 Then 
                    Return a; 
                EndIf.
                foo(1,2,3);
            EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(BinaryOp('+',Id('b'), IntLiteral(0)), [], [Return(Id('a'))])], ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_case_80(self):
        """More complex program"""
        input = """
               Function: main
               Parameter: y, a, x
               Body:
                   x = 1;
                   y = a + foo(x);
               EndBody.
               Function: foo
               Parameter: a
               Body:
                   a = False;
                   Return a;
               EndBody.
               """
        expect = str(TypeMismatchInStatement(Assign(Id('a'), BooleanLiteral(False))))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_case_81(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a
               Body:
                    a = 1.;
                    Return a;
               EndBody.

               Function: foo
               Parameter: a
               Body:
                   a = main(1,2.);
                   a = a + 2;
               EndBody.
               """
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('a'),IntLiteral(2))))
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_case_82(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    For ( i= 1.1 ,i<1000, i+1 ) Do
                    EndFor.
               EndBody.
               """
        expect = str(TypeMismatchInStatement(For(Id('i'), FloatLiteral(1.1), BinaryOp("<", Id("i"), IntLiteral(1000)), BinaryOp("+", Id("i"), IntLiteral(1)), ([],[]))))
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_case_83(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    For ( i= 1 ,i<1000, i+1 ) Do
                        a =  a + x[i][i+1];
                    EndFor.
                    i = i + 1;
               EndBody.
               """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_case_84(self):
        """More complex program"""
        input = """
                Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
               Function: main
               Parameter: y, a, i
               Body:
                    x[1][1.1] = 1;
               EndBody.
               """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'), [IntLiteral(1), FloatLiteral(1.1)])))
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_case_85(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        Return x;
                  EndBody.

                  Function: foo
                  Body:
                        main(1,2,3)[2] = 1;
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(CallExpr(Id('main'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), [IntLiteral(2)])))
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_case_86(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        foo()[2][3] = 0.9;
                        Return x;
                  EndBody.

                  Function: foo
                  Body:
                        Return { { 1.1,2.2, 4.4 }, { 2.2,3.3, 9.9}   }; 
                  EndBody.
                  
                  Function: goo
                  Body:
                        foo()[1][2] = 100;
                  EndBody.
                  """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(2), IntLiteral(3)]),FloatLiteral(0.9))))
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test_case_87(self):
        """More complex program"""
        input = """
                   Var: x[3][2] = { { 1,2 }, { 2,3} , {3,4}   };
                  Function: main
                  Parameter: y, a, i
                  Body:
                        a = 1 + foo();
                  EndBody.

                  Function: foo
                  Body:
                        Return 1.1;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_case_88(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k, a, i
                  Body:
                        Var: bool_of_string;
                        x[1][1][1] = y[2][1];
                        y[1][1] = z[0];
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(ArrayCell(Id('y'),[IntLiteral(1), IntLiteral(1)]), ArrayCell(Id('z'), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_case_89(self):
        input = """
        Var: x[10];
        Function: main
        Body:
            Var: a[10], t, z;
            a[t] = t +. 2.;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('+.',Id('t'),FloatLiteral(2.0))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_case_89(self):
        input = """
        Function: main
        Parameter: x
        Body:
            Var: y, z;
            y = x && (x == z);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp('==',Id('x'),Id('z'))))
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_case_90(self):
        input = """
        Var: a[2] = {0, 1};
        Function: foo
        Parameter: x
        Body:
            Return a;
        EndBody.

        Function: main
            Body:
                foo(0)[0] = foo(0.0)[1 * a[1]];
            EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('foo'),[FloatLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_case_91(self):
        input = """
        Var: a[2] = {0, 1};
        Function: foo
        Parameter: x
        Body:
        EndBody.

        Function: main
            Body:
                foo(0);
                foo("a");
            EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('foo'),[StringLiteral("""a""")])))
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_case_92(self):
        input = """
        Function: foo
        Body:
        EndBody.

        Function: main
        Parameter: x
        Body:
            main(foo());
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[CallExpr(Id('foo'),[])])))
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_case_93(self):
        input = """
        Var: arr[2][3] = {{2, 3, 1}, {3, 1, 0}};
        Function: main
        Parameter: x
        Body:
            arr = {{2, 1}, {7, 3}, {2, 5}};
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('arr'),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(1)]),ArrayLiteral([IntLiteral(7),IntLiteral(3)]),ArrayLiteral([IntLiteral(2),IntLiteral(5)])]))))
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_case_94(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            foo();
            test();
        EndBody.
        Function: test
        Body:
            If x Then
                foo();
            Else
                test();
            EndIf.
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 494))
 
    def test_case_95(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            test();
        EndBody.
        Function: test
        Body:
            If x Then
                foo();
            Else
                test();
            EndIf.
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_case_96(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k[2][2][2], a[3][2], i[1]
                  Body:
                        Var: bool_of_string;
                        k[1] = 1;
                        Return k;
                  EndBody.
                  
                  Function: foo
                  Body:
                        Var: x;
                        x = main( {1}, 2, 3);
                        x = { {1,2} };
                  EndBody.
                  """
        expect = str(TypeMismatchInExpression(ArrayCell(Id('k'),[IntLiteral(1)])))
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_case_97(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { True };
                  Function: main
                  Parameter: k[2][2][2], a[3][2], i[1]
                  Body:
                        k = x;
                        a = y;
                        i = z;
                  EndBody.

                  Function: foo
                  Body:
                        Var: x;
                        main( { { { 100,200 } , {200,300} },  { { 300,400 } , {400,500} } } , { {100,200} , {200,300} , {3,4} } , { False });
                        Return x;
                  EndBody.
                  """
        expect = str(TypeCannotBeInferred(Return(Id('x'))))
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_case_98(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Parameter: k[2][2][2], a[3][2], i[1]
                  Body:
                        k = x;
                        a = y;
                        i = z;
                  EndBody.

                  Function: foo
                  Body:
                        Var: x = 0x9;
                        Var: i = True;
                        main( { { { 100,200 } , {200,300} },  { { 300,400 } , {400,500} } } , { {100,200} , {200,300} , {3,4} } , { 100 });
                        For ( i=2,1<z[1], x+1 ) Do
                            x = 1;
                        EndFor.
                        
                        Return x;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(For(Id('i'), IntLiteral(2), BinaryOp('<', IntLiteral(1), ArrayCell(Id('z'), [IntLiteral(1)])), BinaryOp('+', Id('x'), IntLiteral(1)), ([], [Assign(Id('x'), IntLiteral(1))]))))
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_case_99(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {1,2} , {2,3} , {3,4} }, z[1] = { 1 };
                  Function: main
                  Body:
                        foo();
                        Return y;
                  EndBody.

                  Function: foo
                  Body:
                        Var: y = 0x9;
                        Var: i = True;
                        For ( y = x[1][1][1], 1 < main()[1][1], y + main()[2][0] ) Do
                            y = True;
                        EndFor.

                        Return;
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Assign(Id('y'), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_case_100(self):
        """More complex program"""
        input = """
                   Var: x[2][2][2] = { { { 1,2 } , {2,3} },  { { 3,4 } , {4,5} } };
                   Var: y[3][2] = { {True,False} , {True,False} , {True,True} }, z[1] = { 1 };
                  Function: main
                  Body:
                    foo();
                        Return y;
                  EndBody.

                  Function: foo
                  Body:
                        Var: y = 0x9;
                        Var: i = True;
                        If main()[1][1] Then
                            Return 1;
                        EndIf.
                  EndBody.
                  """
        expect = str(TypeMismatchInStatement(Return(IntLiteral(1))))
        self.assertTrue(TestChecker.test(input, expect, 500))



