# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3J")
        buf.write("\u0208\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0083")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5\u008f")
        buf.write("\n\5\3\6\3\6\5\6\u0093\n\6\3\7\3\7\3\7\3\7\5\7\u0099\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a2\n\b\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00a8\n\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00b0")
        buf.write("\n\n\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00b8\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00c0\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00c7\n\16\3\17\3\17\3\17\3\17\5\17\u00cd\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00d9\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00e0\n\22\3")
        buf.write("\23\3\23\5\23\u00e4\n\23\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u00f8\n\30\3\31\3\31\3\31\3\31\5\31\u00fe\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u0109\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0115\n\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0125\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0132\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0168\n\'\3(\3(\3(")
        buf.write("\3(\3(\3(\5(\u0170\n(\3)\3)\3)\3)\3)\3)\5)\u0178\n)\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\5.\u0194\n.\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\7\60\u019f\n\60\f\60\16\60\u01a2")
        buf.write("\13\60\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u01b5\n\62")
        buf.write("\f\62\16\62\u01b8\13\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\7\63\u01cc\n\63\f\63\16\63\u01cf\13\63\3\64\3\64")
        buf.write("\3\64\5\64\u01d4\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u01db")
        buf.write("\n\65\3\66\3\66\3\66\3\66\3\66\7\66\u01e2\n\66\f\66\16")
        buf.write("\66\u01e5\13\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u01f2\n\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\5=\u0206\n=\3=\2\6^bd")
        buf.write("j>\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2\5\3\2BD")
        buf.write("\4\2&+\63\67\3\2-.\2\u0207\2z\3\2\2\2\4\u0082\3\2\2\2")
        buf.write("\6\u0084\3\2\2\2\b\u008e\3\2\2\2\n\u0092\3\2\2\2\f\u0098")
        buf.write("\3\2\2\2\16\u00a1\3\2\2\2\20\u00a7\3\2\2\2\22\u00af\3")
        buf.write("\2\2\2\24\u00b1\3\2\2\2\26\u00b7\3\2\2\2\30\u00bf\3\2")
        buf.write("\2\2\32\u00c6\3\2\2\2\34\u00cc\3\2\2\2\36\u00ce\3\2\2")
        buf.write("\2 \u00d8\3\2\2\2\"\u00df\3\2\2\2$\u00e3\3\2\2\2&\u00e5")
        buf.write("\3\2\2\2(\u00e7\3\2\2\2*\u00ea\3\2\2\2,\u00f0\3\2\2\2")
        buf.write(".\u00f7\3\2\2\2\60\u00fd\3\2\2\2\62\u0108\3\2\2\2\64\u0114")
        buf.write("\3\2\2\2\66\u0116\3\2\2\28\u0124\3\2\2\2:\u0126\3\2\2")
        buf.write("\2<\u0131\3\2\2\2>\u0133\3\2\2\2@\u0142\3\2\2\2B\u0149")
        buf.write("\3\2\2\2D\u0150\3\2\2\2F\u0153\3\2\2\2H\u0156\3\2\2\2")
        buf.write("J\u015c\3\2\2\2L\u0167\3\2\2\2N\u016f\3\2\2\2P\u0177\3")
        buf.write("\2\2\2R\u0179\3\2\2\2T\u017e\3\2\2\2V\u0184\3\2\2\2X\u018a")
        buf.write("\3\2\2\2Z\u0193\3\2\2\2\\\u0195\3\2\2\2^\u0197\3\2\2\2")
        buf.write("`\u01a3\3\2\2\2b\u01a5\3\2\2\2d\u01b9\3\2\2\2f\u01d3\3")
        buf.write("\2\2\2h\u01da\3\2\2\2j\u01dc\3\2\2\2l\u01f1\3\2\2\2n\u01f3")
        buf.write("\3\2\2\2p\u01f5\3\2\2\2r\u01f7\3\2\2\2t\u01f9\3\2\2\2")
        buf.write("v\u01fb\3\2\2\2x\u0205\3\2\2\2z{\5\4\3\2{|\5\34\17\2|")
        buf.write("}\7\2\2\3}\3\3\2\2\2~\177\5\6\4\2\177\u0080\5\4\3\2\u0080")
        buf.write("\u0083\3\2\2\2\u0081\u0083\3\2\2\2\u0082~\3\2\2\2\u0082")
        buf.write("\u0081\3\2\2\2\u0083\5\3\2\2\2\u0084\u0085\7\33\2\2\u0085")
        buf.write("\u0086\7>\2\2\u0086\u0087\5\b\5\2\u0087\u0088\7A\2\2\u0088")
        buf.write("\7\3\2\2\2\u0089\u008a\5\n\6\2\u008a\u008b\7?\2\2\u008b")
        buf.write("\u008c\5\b\5\2\u008c\u008f\3\2\2\2\u008d\u008f\5\n\6\2")
        buf.write("\u008e\u0089\3\2\2\2\u008e\u008d\3\2\2\2\u008f\t\3\2\2")
        buf.write("\2\u0090\u0093\5\f\7\2\u0091\u0093\5\16\b\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\13\3\2\2\2\u0094\u0099")
        buf.write("\7\6\2\2\u0095\u0096\7\6\2\2\u0096\u0097\7%\2\2\u0097")
        buf.write("\u0099\5\32\16\2\u0098\u0094\3\2\2\2\u0098\u0095\3\2\2")
        buf.write("\2\u0099\r\3\2\2\2\u009a\u009b\7\6\2\2\u009b\u00a2\5\20")
        buf.write("\t\2\u009c\u009d\7\6\2\2\u009d\u009e\5\20\t\2\u009e\u009f")
        buf.write("\7%\2\2\u009f\u00a0\5\32\16\2\u00a0\u00a2\3\2\2\2\u00a1")
        buf.write("\u009a\3\2\2\2\u00a1\u009c\3\2\2\2\u00a2\17\3\2\2\2\u00a3")
        buf.write("\u00a4\5\22\n\2\u00a4\u00a5\5\20\t\2\u00a5\u00a8\3\2\2")
        buf.write("\2\u00a6\u00a8\5\22\n\2\u00a7\u00a3\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\21\3\2\2\2\u00a9\u00aa\7<\2\2\u00aa\u00ab")
        buf.write("\5\24\13\2\u00ab\u00ac\7=\2\2\u00ac\u00b0\3\2\2\2\u00ad")
        buf.write("\u00ae\7<\2\2\u00ae\u00b0\7=\2\2\u00af\u00a9\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00b0\23\3\2\2\2\u00b1\u00b2\t\2\2\2\u00b2")
        buf.write("\25\3\2\2\2\u00b3\u00b4\5\30\r\2\u00b4\u00b5\5\26\f\2")
        buf.write("\u00b5\u00b8\3\2\2\2\u00b6\u00b8\5\30\r\2\u00b7\u00b3")
        buf.write("\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\27\3\2\2\2\u00b9\u00ba")
        buf.write("\7<\2\2\u00ba\u00bb\5Z.\2\u00bb\u00bc\7=\2\2\u00bc\u00c0")
        buf.write("\3\2\2\2\u00bd\u00be\7<\2\2\u00be\u00c0\7=\2\2\u00bf\u00b9")
        buf.write("\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\31\3\2\2\2\u00c1\u00c7")
        buf.write("\5p9\2\u00c2\u00c7\5r:\2\u00c3\u00c7\5t;\2\u00c4\u00c7")
        buf.write("\5v<\2\u00c5\u00c7\5n8\2\u00c6\u00c1\3\2\2\2\u00c6\u00c2")
        buf.write("\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\33\3\2\2\2\u00c8\u00c9\5\36\20\2")
        buf.write("\u00c9\u00ca\5\34\17\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd")
        buf.write("\3\2\2\2\u00cc\u00c8\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\35\3\2\2\2\u00ce\u00cf\7\23\2\2\u00cf\u00d0\7>\2\2\u00d0")
        buf.write("\u00d1\7\6\2\2\u00d1\u00d2\5 \21\2\u00d2\u00d3\5*\26\2")
        buf.write("\u00d3\37\3\2\2\2\u00d4\u00d5\7\26\2\2\u00d5\u00d6\7>")
        buf.write("\2\2\u00d6\u00d9\5\"\22\2\u00d7\u00d9\3\2\2\2\u00d8\u00d4")
        buf.write("\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9!\3\2\2\2\u00da\u00db")
        buf.write("\5$\23\2\u00db\u00dc\7?\2\2\u00dc\u00dd\5\"\22\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00e0\5$\23\2\u00df\u00da\3\2\2\2")
        buf.write("\u00df\u00de\3\2\2\2\u00e0#\3\2\2\2\u00e1\u00e4\5&\24")
        buf.write("\2\u00e2\u00e4\5(\25\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2")
        buf.write("\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6\7\6\2\2\u00e6\'\3")
        buf.write("\2\2\2\u00e7\u00e8\7\6\2\2\u00e8\u00e9\5\20\t\2\u00e9")
        buf.write(")\3\2\2\2\u00ea\u00eb\7\7\2\2\u00eb\u00ec\7>\2\2\u00ec")
        buf.write("\u00ed\5,\27\2\u00ed\u00ee\7\r\2\2\u00ee\u00ef\7@\2\2")
        buf.write("\u00ef+\3\2\2\2\u00f0\u00f1\5.\30\2\u00f1\u00f2\5\60\31")
        buf.write("\2\u00f2-\3\2\2\2\u00f3\u00f4\5\6\4\2\u00f4\u00f5\5.\30")
        buf.write("\2\u00f5\u00f8\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f3")
        buf.write("\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8/\3\2\2\2\u00f9\u00fa")
        buf.write("\5\62\32\2\u00fa\u00fb\5\60\31\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd\u00fc\3\2\2\2")
        buf.write("\u00fe\61\3\2\2\2\u00ff\u0109\5\64\33\2\u0100\u0109\5")
        buf.write("\66\34\2\u0101\u0109\5> \2\u0102\u0109\5@!\2\u0103\u0109")
        buf.write("\5B\"\2\u0104\u0109\5D#\2\u0105\u0109\5F$\2\u0106\u0109")
        buf.write("\5H%\2\u0107\u0109\5N(\2\u0108\u00ff\3\2\2\2\u0108\u0100")
        buf.write("\3\2\2\2\u0108\u0101\3\2\2\2\u0108\u0102\3\2\2\2\u0108")
        buf.write("\u0103\3\2\2\2\u0108\u0104\3\2\2\2\u0108\u0105\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\63\3\2")
        buf.write("\2\2\u010a\u010b\7\6\2\2\u010b\u010c\7%\2\2\u010c\u010d")
        buf.write("\5Z.\2\u010d\u010e\7A\2\2\u010e\u0115\3\2\2\2\u010f\u0110")
        buf.write("\5j\66\2\u0110\u0111\7%\2\2\u0111\u0112\5Z.\2\u0112\u0113")
        buf.write("\7A\2\2\u0113\u0115\3\2\2\2\u0114\u010a\3\2\2\2\u0114")
        buf.write("\u010f\3\2\2\2\u0115\65\3\2\2\2\u0116\u0117\7\25\2\2\u0117")
        buf.write("\u0118\5Z.\2\u0118\u0119\7\30\2\2\u0119\u011a\5.\30\2")
        buf.write("\u011a\u011b\5\60\31\2\u011b\u011c\58\35\2\u011c\u011d")
        buf.write("\5<\37\2\u011d\u011e\7\16\2\2\u011e\u011f\7@\2\2\u011f")
        buf.write("\67\3\2\2\2\u0120\u0121\5:\36\2\u0121\u0122\58\35\2\u0122")
        buf.write("\u0125\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2")
        buf.write("\u0124\u0123\3\2\2\2\u01259\3\2\2\2\u0126\u0127\7\f\2")
        buf.write("\2\u0127\u0128\5Z.\2\u0128\u0129\7\30\2\2\u0129\u012a")
        buf.write("\5.\30\2\u012a\u012b\5\60\31\2\u012b;\3\2\2\2\u012c\u012d")
        buf.write("\7\13\2\2\u012d\u012e\5.\30\2\u012e\u012f\5\60\31\2\u012f")
        buf.write("\u0132\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012c\3\2\2\2")
        buf.write("\u0131\u0130\3\2\2\2\u0132=\3\2\2\2\u0133\u0134\7\22\2")
        buf.write("\2\u0134\u0135\78\2\2\u0135\u0136\7\6\2\2\u0136\u0137")
        buf.write("\7%\2\2\u0137\u0138\5Z.\2\u0138\u0139\7?\2\2\u0139\u013a")
        buf.write("\5Z.\2\u013a\u013b\7?\2\2\u013b\u013c\5Z.\2\u013c\u013d")
        buf.write("\79\2\2\u013d\u013e\7\n\2\2\u013e\u013f\5,\27\2\u013f")
        buf.write("\u0140\7\17\2\2\u0140\u0141\7@\2\2\u0141?\3\2\2\2\u0142")
        buf.write("\u0143\7\32\2\2\u0143\u0144\5Z.\2\u0144\u0145\7\n\2\2")
        buf.write("\u0145\u0146\5,\27\2\u0146\u0147\7\21\2\2\u0147\u0148")
        buf.write("\7@\2\2\u0148A\3\2\2\2\u0149\u014a\7\n\2\2\u014a\u014b")
        buf.write("\5,\27\2\u014b\u014c\7\32\2\2\u014c\u014d\5Z.\2\u014d")
        buf.write("\u014e\7\20\2\2\u014e\u014f\7@\2\2\u014fC\3\2\2\2\u0150")
        buf.write("\u0151\7\b\2\2\u0151\u0152\7A\2\2\u0152E\3\2\2\2\u0153")
        buf.write("\u0154\7\t\2\2\u0154\u0155\7A\2\2\u0155G\3\2\2\2\u0156")
        buf.write("\u0157\7\6\2\2\u0157\u0158\78\2\2\u0158\u0159\5L\'\2\u0159")
        buf.write("\u015a\79\2\2\u015a\u015b\7A\2\2\u015bI\3\2\2\2\u015c")
        buf.write("\u015d\7\6\2\2\u015d\u015e\78\2\2\u015e\u015f\5L\'\2\u015f")
        buf.write("\u0160\79\2\2\u0160K\3\2\2\2\u0161\u0162\5Z.\2\u0162\u0163")
        buf.write("\7?\2\2\u0163\u0164\5L\'\2\u0164\u0168\3\2\2\2\u0165\u0168")
        buf.write("\5Z.\2\u0166\u0168\3\2\2\2\u0167\u0161\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168M\3\2\2\2\u0169\u016a")
        buf.write("\7\27\2\2\u016a\u016b\5Z.\2\u016b\u016c\7A\2\2\u016c\u0170")
        buf.write("\3\2\2\2\u016d\u016e\7\27\2\2\u016e\u0170\7A\2\2\u016f")
        buf.write("\u0169\3\2\2\2\u016f\u016d\3\2\2\2\u0170O\3\2\2\2\u0171")
        buf.write("\u0178\5R*\2\u0172\u0178\5T+\2\u0173\u0178\5V,\2\u0174")
        buf.write("\u0175\5X-\2\u0175\u0176\7A\2\2\u0176\u0178\3\2\2\2\u0177")
        buf.write("\u0171\3\2\2\2\u0177\u0172\3\2\2\2\u0177\u0173\3\2\2\2")
        buf.write("\u0177\u0174\3\2\2\2\u0178Q\3\2\2\2\u0179\u017a\7\34\2")
        buf.write("\2\u017a\u017b\78\2\2\u017b\u017c\79\2\2\u017c\u017d\7")
        buf.write("A\2\2\u017dS\3\2\2\2\u017e\u017f\7\35\2\2\u017f\u0180")
        buf.write("\78\2\2\u0180\u0181\5Z.\2\u0181\u0182\79\2\2\u0182\u0183")
        buf.write("\7A\2\2\u0183U\3\2\2\2\u0184\u0185\7\36\2\2\u0185\u0186")
        buf.write("\78\2\2\u0186\u0187\5Z.\2\u0187\u0188\79\2\2\u0188\u0189")
        buf.write("\7A\2\2\u0189W\3\2\2\2\u018a\u018b\7\37\2\2\u018b\u018c")
        buf.write("\78\2\2\u018c\u018d\79\2\2\u018dY\3\2\2\2\u018e\u018f")
        buf.write("\5^\60\2\u018f\u0190\5\\/\2\u0190\u0191\5^\60\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0194\5^\60\2\u0193\u018e\3\2\2\2")
        buf.write("\u0193\u0192\3\2\2\2\u0194[\3\2\2\2\u0195\u0196\t\3\2")
        buf.write("\2\u0196]\3\2\2\2\u0197\u0198\b\60\1\2\u0198\u0199\5b")
        buf.write("\62\2\u0199\u01a0\3\2\2\2\u019a\u019b\f\4\2\2\u019b\u019c")
        buf.write("\5`\61\2\u019c\u019d\5b\62\2\u019d\u019f\3\2\2\2\u019e")
        buf.write("\u019a\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1_\3\2\2\2\u01a2\u01a0\3\2\2")
        buf.write("\2\u01a3\u01a4\t\4\2\2\u01a4a\3\2\2\2\u01a5\u01a6\b\62")
        buf.write("\1\2\u01a6\u01a7\5d\63\2\u01a7\u01b6\3\2\2\2\u01a8\u01a9")
        buf.write("\f\7\2\2\u01a9\u01aa\7 \2\2\u01aa\u01b5\5d\63\2\u01ab")
        buf.write("\u01ac\f\6\2\2\u01ac\u01ad\7!\2\2\u01ad\u01b5\5d\63\2")
        buf.write("\u01ae\u01af\f\5\2\2\u01af\u01b0\7/\2\2\u01b0\u01b5\5")
        buf.write("d\63\2\u01b1\u01b2\f\4\2\2\u01b2\u01b3\7\60\2\2\u01b3")
        buf.write("\u01b5\5d\63\2\u01b4\u01a8\3\2\2\2\u01b4\u01ab\3\2\2\2")
        buf.write("\u01b4\u01ae\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b5\u01b8\3")
        buf.write("\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7c")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\b\63\1\2\u01ba")
        buf.write("\u01bb\5f\64\2\u01bb\u01cd\3\2\2\2\u01bc\u01bd\f\b\2\2")
        buf.write("\u01bd\u01be\7\"\2\2\u01be\u01cc\5f\64\2\u01bf\u01c0\f")
        buf.write("\7\2\2\u01c0\u01c1\7#\2\2\u01c1\u01cc\5f\64\2\u01c2\u01c3")
        buf.write("\f\6\2\2\u01c3\u01c4\7$\2\2\u01c4\u01cc\5f\64\2\u01c5")
        buf.write("\u01c6\f\5\2\2\u01c6\u01c7\7\61\2\2\u01c7\u01cc\5f\64")
        buf.write("\2\u01c8\u01c9\f\4\2\2\u01c9\u01ca\7\62\2\2\u01ca\u01cc")
        buf.write("\5f\64\2\u01cb\u01bc\3\2\2\2\u01cb\u01bf\3\2\2\2\u01cb")
        buf.write("\u01c2\3\2\2\2\u01cb\u01c5\3\2\2\2\u01cb\u01c8\3\2\2\2")
        buf.write("\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01cee\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1")
        buf.write("\7,\2\2\u01d1\u01d4\5f\64\2\u01d2\u01d4\5h\65\2\u01d3")
        buf.write("\u01d0\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4g\3\2\2\2\u01d5")
        buf.write("\u01d6\7!\2\2\u01d6\u01db\5h\65\2\u01d7\u01d8\7\60\2\2")
        buf.write("\u01d8\u01db\5h\65\2\u01d9\u01db\5j\66\2\u01da\u01d5\3")
        buf.write("\2\2\2\u01da\u01d7\3\2\2\2\u01da\u01d9\3\2\2\2\u01dbi")
        buf.write("\3\2\2\2\u01dc\u01dd\b\66\1\2\u01dd\u01de\5l\67\2\u01de")
        buf.write("\u01e3\3\2\2\2\u01df\u01e0\f\4\2\2\u01e0\u01e2\5\26\f")
        buf.write("\2\u01e1\u01df\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4k\3\2\2\2\u01e5\u01e3")
        buf.write("\3\2\2\2\u01e6\u01f2\5p9\2\u01e7\u01f2\5r:\2\u01e8\u01f2")
        buf.write("\5n8\2\u01e9\u01f2\5v<\2\u01ea\u01f2\5t;\2\u01eb\u01f2")
        buf.write("\7\6\2\2\u01ec\u01f2\5J&\2\u01ed\u01ee\78\2\2\u01ee\u01ef")
        buf.write("\5Z.\2\u01ef\u01f0\79\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01e6")
        buf.write("\3\2\2\2\u01f1\u01e7\3\2\2\2\u01f1\u01e8\3\2\2\2\u01f1")
        buf.write("\u01e9\3\2\2\2\u01f1\u01ea\3\2\2\2\u01f1\u01eb\3\2\2\2")
        buf.write("\u01f1\u01ec\3\2\2\2\u01f1\u01ed\3\2\2\2\u01f2m\3\2\2")
        buf.write("\2\u01f3\u01f4\7\3\2\2\u01f4o\3\2\2\2\u01f5\u01f6\t\2")
        buf.write("\2\2\u01f6q\3\2\2\2\u01f7\u01f8\7E\2\2\u01f8s\3\2\2\2")
        buf.write("\u01f9\u01fa\7F\2\2\u01fau\3\2\2\2\u01fb\u01fc\7:\2\2")
        buf.write("\u01fc\u01fd\5x=\2\u01fd\u01fe\7;\2\2\u01few\3\2\2\2\u01ff")
        buf.write("\u0200\5\32\16\2\u0200\u0201\7?\2\2\u0201\u0202\5x=\2")
        buf.write("\u0202\u0206\3\2\2\2\u0203\u0206\5\32\16\2\u0204\u0206")
        buf.write("\3\2\2\2\u0205\u01ff\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0204\3\2\2\2\u0206y\3\2\2\2$\u0082\u008e\u0092\u0098")
        buf.write("\u00a1\u00a7\u00af\u00b7\u00bf\u00c6\u00cc\u00d8\u00df")
        buf.write("\u00e3\u00f7\u00fd\u0108\u0114\u0124\u0131\u0167\u016f")
        buf.write("\u0177\u0193\u01a0\u01b4\u01b6\u01cb\u01cd\u01d3\u01da")
        buf.write("\u01e3\u01f1\u0205")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
                     "'EndDo'", "'EndWhile'", "'For'", "'Function'", "'False'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'True'", 
                     "'While'", "'Var'", "'printLn'", "'print'", "'printStrLn'", 
                     "'read'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'='", 
                     "'<'", "'>'", "'<='", "'>='", "'!='", "'=='", "'!'", 
                     "'&&'", "'||'", "'+.'", "'-.'", "'*.'", "'\\.'", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "'=/='", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "':'", "','", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>", "BOOL_LIT", "WS", "CMT", "ID", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDDO", "ENDWHILE", "FOR", "FUNCTION", 
                      "FALSE", "IF", "PARAMETER", "RETURN", "THEN", "TRUE", 
                      "WHILE", "VAR", "PRINTLN", "PRINT", "PRINTSTRLN", 
                      "READ", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "LESS", 
                      "GREATER", "LESS_EQ", "GREATER_EQ", "NOT_EQ", "EQ_RELATION", 
                      "NOT", "AND", "OR", "F_ADD", "F_SUB", "F_MUL", "F_DIV", 
                      "F_LESS", "F_GREATER", "F_LESS_EQ", "F_GREATER_EQ", 
                      "F_NOT_EQ", "LP", "RP", "LB", "RB", "LSB", "RSB", 
                      "COLON", "CM", "DOT", "SM", "INT_HEXA", "INT_OCTO", 
                      "INT_DECE", "FLOAT_LIT", "STRING_LIT", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_declars_part = 1
    RULE_var_declar = 2
    RULE_var_list = 3
    RULE_variable = 4
    RULE_scalar = 5
    RULE_composite = 6
    RULE_dimensions_of_var = 7
    RULE_dimen_of_var = 8
    RULE_int_lit_dimen = 9
    RULE_dimensions = 10
    RULE_dimen = 11
    RULE_init_value = 12
    RULE_func_declars_part = 13
    RULE_func_declar = 14
    RULE_para_declar = 15
    RULE_list_para = 16
    RULE_para = 17
    RULE_scalar_para = 18
    RULE_composite_para = 19
    RULE_body_declar = 20
    RULE_list_stmts = 21
    RULE_list_var_stmts = 22
    RULE_list_other_stmts = 23
    RULE_stmt = 24
    RULE_assign_stmt = 25
    RULE_if_stmt = 26
    RULE_list_elseif = 27
    RULE_el_if = 28
    RULE_case_else = 29
    RULE_for_stmt = 30
    RULE_while_stmt = 31
    RULE_do_stmt = 32
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_call_stmt = 35
    RULE_call = 36
    RULE_list_args = 37
    RULE_return_stmt = 38
    RULE_builtin_func = 39
    RULE_print_ln = 40
    RULE_print_func = 41
    RULE_print_str_ln = 42
    RULE_read = 43
    RULE_relation = 44
    RULE_relation_op = 45
    RULE_logical = 46
    RULE_logical_op = 47
    RULE_exp = 48
    RULE_exp2 = 49
    RULE_exp3 = 50
    RULE_exp4 = 51
    RULE_exp5 = 52
    RULE_exp6 = 53
    RULE_bool_lit = 54
    RULE_int_lit = 55
    RULE_float_lit = 56
    RULE_string_lit = 57
    RULE_array_lit = 58
    RULE_array_lit_element = 59

    ruleNames =  [ "program", "var_declars_part", "var_declar", "var_list", 
                   "variable", "scalar", "composite", "dimensions_of_var", 
                   "dimen_of_var", "int_lit_dimen", "dimensions", "dimen", 
                   "init_value", "func_declars_part", "func_declar", "para_declar", 
                   "list_para", "para", "scalar_para", "composite_para", 
                   "body_declar", "list_stmts", "list_var_stmts", "list_other_stmts", 
                   "stmt", "assign_stmt", "if_stmt", "list_elseif", "el_if", 
                   "case_else", "for_stmt", "while_stmt", "do_stmt", "break_stmt", 
                   "continue_stmt", "call_stmt", "call", "list_args", "return_stmt", 
                   "builtin_func", "print_ln", "print_func", "print_str_ln", 
                   "read", "relation", "relation_op", "logical", "logical_op", 
                   "exp", "exp2", "exp3", "exp4", "exp5", "exp6", "bool_lit", 
                   "int_lit", "float_lit", "string_lit", "array_lit", "array_lit_element" ]

    EOF = Token.EOF
    BOOL_LIT=1
    WS=2
    CMT=3
    ID=4
    BODY=5
    BREAK=6
    CONTINUE=7
    DO=8
    ELSE=9
    ELSEIF=10
    ENDBODY=11
    ENDIF=12
    ENDFOR=13
    ENDDO=14
    ENDWHILE=15
    FOR=16
    FUNCTION=17
    FALSE=18
    IF=19
    PARAMETER=20
    RETURN=21
    THEN=22
    TRUE=23
    WHILE=24
    VAR=25
    PRINTLN=26
    PRINT=27
    PRINTSTRLN=28
    READ=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34
    EQ=35
    LESS=36
    GREATER=37
    LESS_EQ=38
    GREATER_EQ=39
    NOT_EQ=40
    EQ_RELATION=41
    NOT=42
    AND=43
    OR=44
    F_ADD=45
    F_SUB=46
    F_MUL=47
    F_DIV=48
    F_LESS=49
    F_GREATER=50
    F_LESS_EQ=51
    F_GREATER_EQ=52
    F_NOT_EQ=53
    LP=54
    RP=55
    LB=56
    RB=57
    LSB=58
    RSB=59
    COLON=60
    CM=61
    DOT=62
    SM=63
    INT_HEXA=64
    INT_OCTO=65
    INT_DECE=66
    FLOAT_LIT=67
    STRING_LIT=68
    ILLEGAL_ESCAPE=69
    UNCLOSE_STRING=70
    ERROR_CHAR=71
    UNTERMINATED_COMMENT=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declars_part(self):
            return self.getTypedRuleContext(BKITParser.Var_declars_partContext,0)


        def func_declars_part(self):
            return self.getTypedRuleContext(BKITParser.Func_declars_partContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.var_declars_part()
            self.state = 121
            self.func_declars_part()
            self.state = 122
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declars_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declar(self):
            return self.getTypedRuleContext(BKITParser.Var_declarContext,0)


        def var_declars_part(self):
            return self.getTypedRuleContext(BKITParser.Var_declars_partContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declars_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declars_part" ):
                return visitor.visitVar_declars_part(self)
            else:
                return visitor.visitChildren(self)




    def var_declars_part(self):

        localctx = BKITParser.Var_declars_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declars_part)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.var_declar()
                self.state = 125
                self.var_declars_part()
                pass
            elif token in [BKITParser.EOF, BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declar" ):
                return visitor.visitVar_declar(self)
            else:
                return visitor.visitChildren(self)




    def var_declar(self):

        localctx = BKITParser.Var_declarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(BKITParser.VAR)
            self.state = 131
            self.match(BKITParser.COLON)
            self.state = 132
            self.var_list()
            self.state = 133
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_list)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.variable()
                self.state = 136
                self.match(BKITParser.CM)
                self.state = 137
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self):
            return self.getTypedRuleContext(BKITParser.ScalarContext,0)


        def composite(self):
            return self.getTypedRuleContext(BKITParser.CompositeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.scalar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.composite()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)




    def scalar(self):

        localctx = BKITParser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_scalar)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(BKITParser.ID)
                self.state = 148
                self.match(BKITParser.EQ)
                self.state = 149
                self.init_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimensions_of_var(self):
            return self.getTypedRuleContext(BKITParser.Dimensions_of_varContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite" ):
                return visitor.visitComposite(self)
            else:
                return visitor.visitChildren(self)




    def composite(self):

        localctx = BKITParser.CompositeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_composite)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(BKITParser.ID)
                self.state = 153
                self.dimensions_of_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(BKITParser.ID)
                self.state = 155
                self.dimensions_of_var()
                self.state = 156
                self.match(BKITParser.EQ)
                self.state = 157
                self.init_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimensions_of_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimen_of_var(self):
            return self.getTypedRuleContext(BKITParser.Dimen_of_varContext,0)


        def dimensions_of_var(self):
            return self.getTypedRuleContext(BKITParser.Dimensions_of_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimensions_of_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions_of_var" ):
                return visitor.visitDimensions_of_var(self)
            else:
                return visitor.visitChildren(self)




    def dimensions_of_var(self):

        localctx = BKITParser.Dimensions_of_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dimensions_of_var)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.dimen_of_var()
                self.state = 162
                self.dimensions_of_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.dimen_of_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimen_of_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def int_lit_dimen(self):
            return self.getTypedRuleContext(BKITParser.Int_lit_dimenContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimen_of_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimen_of_var" ):
                return visitor.visitDimen_of_var(self)
            else:
                return visitor.visitChildren(self)




    def dimen_of_var(self):

        localctx = BKITParser.Dimen_of_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dimen_of_var)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(BKITParser.LSB)
                self.state = 168
                self.int_lit_dimen()
                self.state = 169
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(BKITParser.LSB)
                self.state = 172
                self.match(BKITParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_lit_dimenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_DECE(self):
            return self.getToken(BKITParser.INT_DECE, 0)

        def INT_HEXA(self):
            return self.getToken(BKITParser.INT_HEXA, 0)

        def INT_OCTO(self):
            return self.getToken(BKITParser.INT_OCTO, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_lit_dimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit_dimen" ):
                return visitor.visitInt_lit_dimen(self)
            else:
                return visitor.visitChildren(self)




    def int_lit_dimen(self):

        localctx = BKITParser.Int_lit_dimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_int_lit_dimen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.INT_HEXA - 64)) | (1 << (BKITParser.INT_OCTO - 64)) | (1 << (BKITParser.INT_DECE - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimen(self):
            return self.getTypedRuleContext(BKITParser.DimenContext,0)


        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = BKITParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dimensions)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.dimen()
                self.state = 178
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.dimen()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimen" ):
                return visitor.visitDimen(self)
            else:
                return visitor.visitChildren(self)




    def dimen(self):

        localctx = BKITParser.DimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dimen)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(BKITParser.LSB)
                self.state = 184
                self.relation()
                self.state = 185
                self.match(BKITParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(BKITParser.LSB)
                self.state = 188
                self.match(BKITParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(BKITParser.Int_litContext,0)


        def float_lit(self):
            return self.getTypedRuleContext(BKITParser.Float_litContext,0)


        def string_lit(self):
            return self.getTypedRuleContext(BKITParser.String_litContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def bool_lit(self):
            return self.getTypedRuleContext(BKITParser.Bool_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_init_value)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT_HEXA, BKITParser.INT_OCTO, BKITParser.INT_DECE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.int_lit()
                pass
            elif token in [BKITParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.float_lit()
                pass
            elif token in [BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.string_lit()
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.array_lit()
                pass
            elif token in [BKITParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.bool_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declars_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_declar(self):
            return self.getTypedRuleContext(BKITParser.Func_declarContext,0)


        def func_declars_part(self):
            return self.getTypedRuleContext(BKITParser.Func_declars_partContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declars_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declars_part" ):
                return visitor.visitFunc_declars_part(self)
            else:
                return visitor.visitChildren(self)




    def func_declars_part(self):

        localctx = BKITParser.Func_declars_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_declars_part)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.func_declar()
                self.state = 199
                self.func_declars_part()
                pass
            elif token in [BKITParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def para_declar(self):
            return self.getTypedRuleContext(BKITParser.Para_declarContext,0)


        def body_declar(self):
            return self.getTypedRuleContext(BKITParser.Body_declarContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declar" ):
                return visitor.visitFunc_declar(self)
            else:
                return visitor.visitChildren(self)




    def func_declar(self):

        localctx = BKITParser.Func_declarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_declar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BKITParser.FUNCTION)
            self.state = 205
            self.match(BKITParser.COLON)
            self.state = 206
            self.match(BKITParser.ID)
            self.state = 207
            self.para_declar()
            self.state = 208
            self.body_declar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def list_para(self):
            return self.getTypedRuleContext(BKITParser.List_paraContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para_declar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_declar" ):
                return visitor.visitPara_declar(self)
            else:
                return visitor.visitChildren(self)




    def para_declar(self):

        localctx = BKITParser.Para_declarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_para_declar)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.PARAMETER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(BKITParser.PARAMETER)
                self.state = 211
                self.match(BKITParser.COLON)
                self.state = 212
                self.list_para()
                pass
            elif token in [BKITParser.BODY]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(BKITParser.ParaContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def list_para(self):
            return self.getTypedRuleContext(BKITParser.List_paraContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = BKITParser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_para)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.para()
                self.state = 217
                self.match(BKITParser.CM)
                self.state = 218
                self.list_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_para(self):
            return self.getTypedRuleContext(BKITParser.Scalar_paraContext,0)


        def composite_para(self):
            return self.getTypedRuleContext(BKITParser.Composite_paraContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = BKITParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_para)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.scalar_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.composite_para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scalar_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_para" ):
                return visitor.visitScalar_para(self)
            else:
                return visitor.visitChildren(self)




    def scalar_para(self):

        localctx = BKITParser.Scalar_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_scalar_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimensions_of_var(self):
            return self.getTypedRuleContext(BKITParser.Dimensions_of_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_para" ):
                return visitor.visitComposite_para(self)
            else:
                return visitor.visitChildren(self)




    def composite_para(self):

        localctx = BKITParser.Composite_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_composite_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(BKITParser.ID)
            self.state = 230
            self.dimensions_of_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_declarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_stmtsContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body_declar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_declar" ):
                return visitor.visitBody_declar(self)
            else:
                return visitor.visitChildren(self)




    def body_declar(self):

        localctx = BKITParser.Body_declarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_body_declar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKITParser.BODY)
            self.state = 233
            self.match(BKITParser.COLON)
            self.state = 234
            self.list_stmts()
            self.state = 235
            self.match(BKITParser.ENDBODY)
            self.state = 236
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_var_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_var_stmtsContext,0)


        def list_other_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_other_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmts" ):
                return visitor.visitList_stmts(self)
            else:
                return visitor.visitChildren(self)




    def list_stmts(self):

        localctx = BKITParser.List_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_stmts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.list_var_stmts()
            self.state = 239
            self.list_other_stmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_var_stmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declar(self):
            return self.getTypedRuleContext(BKITParser.Var_declarContext,0)


        def list_var_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_var_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_var_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_var_stmts" ):
                return visitor.visitList_var_stmts(self)
            else:
                return visitor.visitChildren(self)




    def list_var_stmts(self):

        localctx = BKITParser.List_var_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_var_stmts)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.var_declar()
                self.state = 242
                self.list_var_stmts()
                pass
            elif token in [BKITParser.BOOL_LIT, BKITParser.ID, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.DO, BKITParser.ELSE, BKITParser.ELSEIF, BKITParser.ENDBODY, BKITParser.ENDIF, BKITParser.ENDFOR, BKITParser.ENDWHILE, BKITParser.FOR, BKITParser.IF, BKITParser.RETURN, BKITParser.WHILE, BKITParser.LP, BKITParser.LB, BKITParser.INT_HEXA, BKITParser.INT_OCTO, BKITParser.INT_DECE, BKITParser.FLOAT_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_other_stmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKITParser.StmtContext,0)


        def list_other_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_other_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_other_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_other_stmts" ):
                return visitor.visitList_other_stmts(self)
            else:
                return visitor.visitChildren(self)




    def list_other_stmts(self):

        localctx = BKITParser.List_other_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_list_other_stmts)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.stmt()
                self.state = 248
                self.list_other_stmts()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.do_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 259
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 260
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 261
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assign_stmt)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(BKITParser.ID)
                self.state = 265
                self.match(BKITParser.EQ)
                self.state = 266
                self.relation()
                self.state = 267
                self.match(BKITParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.exp5(0)
                self.state = 270
                self.match(BKITParser.EQ)
                self.state = 271
                self.relation()
                self.state = 272
                self.match(BKITParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def list_var_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_var_stmtsContext,0)


        def list_other_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_other_stmtsContext,0)


        def list_elseif(self):
            return self.getTypedRuleContext(BKITParser.List_elseifContext,0)


        def case_else(self):
            return self.getTypedRuleContext(BKITParser.Case_elseContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(BKITParser.IF)
            self.state = 277
            self.relation()
            self.state = 278
            self.match(BKITParser.THEN)
            self.state = 279
            self.list_var_stmts()
            self.state = 280
            self.list_other_stmts()
            self.state = 281
            self.list_elseif()
            self.state = 282
            self.case_else()
            self.state = 283
            self.match(BKITParser.ENDIF)
            self.state = 284
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elseifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def el_if(self):
            return self.getTypedRuleContext(BKITParser.El_ifContext,0)


        def list_elseif(self):
            return self.getTypedRuleContext(BKITParser.List_elseifContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_elseif" ):
                return visitor.visitList_elseif(self)
            else:
                return visitor.visitChildren(self)




    def list_elseif(self):

        localctx = BKITParser.List_elseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_list_elseif)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.el_if()
                self.state = 287
                self.list_elseif()
                pass
            elif token in [BKITParser.ELSE, BKITParser.ENDIF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class El_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def list_var_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_var_stmtsContext,0)


        def list_other_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_other_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_el_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEl_if" ):
                return visitor.visitEl_if(self)
            else:
                return visitor.visitChildren(self)




    def el_if(self):

        localctx = BKITParser.El_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_el_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKITParser.ELSEIF)
            self.state = 293
            self.relation()
            self.state = 294
            self.match(BKITParser.THEN)
            self.state = 295
            self.list_var_stmts()
            self.state = 296
            self.list_other_stmts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_elseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def list_var_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_var_stmtsContext,0)


        def list_other_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_other_stmtsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_case_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_else" ):
                return visitor.visitCase_else(self)
            else:
                return visitor.visitChildren(self)




    def case_else(self):

        localctx = BKITParser.Case_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_case_else)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(BKITParser.ELSE)
                self.state = 299
                self.list_var_stmts()
                self.state = 300
                self.list_other_stmts()
                pass
            elif token in [BKITParser.ENDIF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.RelationContext)
            else:
                return self.getTypedRuleContext(BKITParser.RelationContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_stmtsContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(BKITParser.FOR)
            self.state = 306
            self.match(BKITParser.LP)
            self.state = 307
            self.match(BKITParser.ID)
            self.state = 308
            self.match(BKITParser.EQ)
            self.state = 309
            self.relation()
            self.state = 310
            self.match(BKITParser.CM)
            self.state = 311
            self.relation()
            self.state = 312
            self.match(BKITParser.CM)
            self.state = 313
            self.relation()
            self.state = 314
            self.match(BKITParser.RP)
            self.state = 315
            self.match(BKITParser.DO)
            self.state = 316
            self.list_stmts()
            self.state = 317
            self.match(BKITParser.ENDFOR)
            self.state = 318
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_stmtsContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(BKITParser.WHILE)
            self.state = 321
            self.relation()
            self.state = 322
            self.match(BKITParser.DO)
            self.state = 323
            self.list_stmts()
            self.state = 324
            self.match(BKITParser.ENDWHILE)
            self.state = 325
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def list_stmts(self):
            return self.getTypedRuleContext(BKITParser.List_stmtsContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_stmt" ):
                return visitor.visitDo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_stmt(self):

        localctx = BKITParser.Do_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_do_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(BKITParser.DO)
            self.state = 328
            self.list_stmts()
            self.state = 329
            self.match(BKITParser.WHILE)
            self.state = 330
            self.relation()
            self.state = 331
            self.match(BKITParser.ENDDO)
            self.state = 332
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BKITParser.BREAK)
            self.state = 335
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BKITParser.CONTINUE)
            self.state = 338
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def list_args(self):
            return self.getTypedRuleContext(BKITParser.List_argsContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(BKITParser.ID)
            self.state = 341
            self.match(BKITParser.LP)
            self.state = 342
            self.list_args()
            self.state = 343
            self.match(BKITParser.RP)
            self.state = 344
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def list_args(self):
            return self.getTypedRuleContext(BKITParser.List_argsContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = BKITParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(BKITParser.ID)
            self.state = 347
            self.match(BKITParser.LP)
            self.state = 348
            self.list_args()
            self.state = 349
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def list_args(self):
            return self.getTypedRuleContext(BKITParser.List_argsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_list_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_args" ):
                return visitor.visitList_args(self)
            else:
                return visitor.visitChildren(self)




    def list_args(self):

        localctx = BKITParser.List_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_args)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.relation()
                self.state = 352
                self.match(BKITParser.CM)
                self.state = 353
                self.list_args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.relation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_stmt)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(BKITParser.RETURN)
                self.state = 360
                self.relation()
                self.state = 361
                self.match(BKITParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(BKITParser.RETURN)
                self.state = 364
                self.match(BKITParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_ln(self):
            return self.getTypedRuleContext(BKITParser.Print_lnContext,0)


        def print_func(self):
            return self.getTypedRuleContext(BKITParser.Print_funcContext,0)


        def print_str_ln(self):
            return self.getTypedRuleContext(BKITParser.Print_str_lnContext,0)


        def read(self):
            return self.getTypedRuleContext(BKITParser.ReadContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_builtin_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltin_func" ):
                return visitor.visitBuiltin_func(self)
            else:
                return visitor.visitChildren(self)




    def builtin_func(self):

        localctx = BKITParser.Builtin_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_builtin_func)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.PRINTLN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.print_ln()
                pass
            elif token in [BKITParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.print_func()
                pass
            elif token in [BKITParser.PRINTSTRLN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.print_str_ln()
                pass
            elif token in [BKITParser.READ]:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.read()
                self.state = 371
                self.match(BKITParser.SM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_lnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(BKITParser.PRINTLN, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_print_ln

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_ln" ):
                return visitor.visitPrint_ln(self)
            else:
                return visitor.visitChildren(self)




    def print_ln(self):

        localctx = BKITParser.Print_lnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_print_ln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(BKITParser.PRINTLN)
            self.state = 376
            self.match(BKITParser.LP)
            self.state = 377
            self.match(BKITParser.RP)
            self.state = 378
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BKITParser.PRINT, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_print_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_func" ):
                return visitor.visitPrint_func(self)
            else:
                return visitor.visitChildren(self)




    def print_func(self):

        localctx = BKITParser.Print_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_print_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(BKITParser.PRINT)
            self.state = 381
            self.match(BKITParser.LP)
            self.state = 382
            self.relation()
            self.state = 383
            self.match(BKITParser.RP)
            self.state = 384
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_str_lnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTSTRLN(self):
            return self.getToken(BKITParser.PRINTSTRLN, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_print_str_ln

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_str_ln" ):
                return visitor.visitPrint_str_ln(self)
            else:
                return visitor.visitChildren(self)




    def print_str_ln(self):

        localctx = BKITParser.Print_str_lnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_print_str_ln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(BKITParser.PRINTSTRLN)
            self.state = 387
            self.match(BKITParser.LP)
            self.state = 388
            self.relation()
            self.state = 389
            self.match(BKITParser.RP)
            self.state = 390
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(BKITParser.READ, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_read

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = BKITParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(BKITParser.READ)
            self.state = 393
            self.match(BKITParser.LP)
            self.state = 394
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LogicalContext)
            else:
                return self.getTypedRuleContext(BKITParser.LogicalContext,i)


        def relation_op(self):
            return self.getTypedRuleContext(BKITParser.Relation_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_relation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = BKITParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_relation)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.logical(0)
                self.state = 397
                self.relation_op()
                self.state = 398
                self.logical(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.logical(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_RELATION(self):
            return self.getToken(BKITParser.EQ_RELATION, 0)

        def NOT_EQ(self):
            return self.getToken(BKITParser.NOT_EQ, 0)

        def LESS(self):
            return self.getToken(BKITParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKITParser.GREATER, 0)

        def LESS_EQ(self):
            return self.getToken(BKITParser.LESS_EQ, 0)

        def GREATER_EQ(self):
            return self.getToken(BKITParser.GREATER_EQ, 0)

        def F_NOT_EQ(self):
            return self.getToken(BKITParser.F_NOT_EQ, 0)

        def F_LESS(self):
            return self.getToken(BKITParser.F_LESS, 0)

        def F_GREATER(self):
            return self.getToken(BKITParser.F_GREATER, 0)

        def F_LESS_EQ(self):
            return self.getToken(BKITParser.F_LESS_EQ, 0)

        def F_GREATER_EQ(self):
            return self.getToken(BKITParser.F_GREATER_EQ, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relation_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_op" ):
                return visitor.visitRelation_op(self)
            else:
                return visitor.visitChildren(self)




    def relation_op(self):

        localctx = BKITParser.Relation_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_relation_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LESS) | (1 << BKITParser.GREATER) | (1 << BKITParser.LESS_EQ) | (1 << BKITParser.GREATER_EQ) | (1 << BKITParser.NOT_EQ) | (1 << BKITParser.EQ_RELATION) | (1 << BKITParser.F_LESS) | (1 << BKITParser.F_GREATER) | (1 << BKITParser.F_LESS_EQ) | (1 << BKITParser.F_GREATER_EQ) | (1 << BKITParser.F_NOT_EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def logical(self):
            return self.getTypedRuleContext(BKITParser.LogicalContext,0)


        def logical_op(self):
            return self.getTypedRuleContext(BKITParser.Logical_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)



    def logical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.LogicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_logical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.exp(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 414
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.LogicalContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical)
                    self.state = 408
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    self.logical_op()
                    self.state = 410
                    self.exp(0) 
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_logical_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_op" ):
                return visitor.visitLogical_op(self)
            else:
                return visitor.visitChildren(self)




    def logical_op(self):

        localctx = BKITParser.Logical_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_logical_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            _la = self._input.LA(1)
            if not(_la==BKITParser.AND or _la==BKITParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def F_ADD(self):
            return self.getToken(BKITParser.F_ADD, 0)

        def F_SUB(self):
            return self.getToken(BKITParser.F_SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 434
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 422
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 423
                        self.match(BKITParser.ADD)
                        self.state = 424
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 425
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 426
                        self.match(BKITParser.SUB)
                        self.state = 427
                        self.exp2(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 428
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 429
                        self.match(BKITParser.F_ADD)
                        self.state = 430
                        self.exp2(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 431
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 432
                        self.match(BKITParser.F_SUB)
                        self.state = 433
                        self.exp2(0)
                        pass

             
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def F_MUL(self):
            return self.getToken(BKITParser.F_MUL, 0)

        def F_DIV(self):
            return self.getToken(BKITParser.F_DIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 457
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 442
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 443
                        self.match(BKITParser.MUL)
                        self.state = 444
                        self.exp3()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 445
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 446
                        self.match(BKITParser.DIV)
                        self.state = 447
                        self.exp3()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 448
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 449
                        self.match(BKITParser.MOD)
                        self.state = 450
                        self.exp3()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 451
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 452
                        self.match(BKITParser.F_MUL)
                        self.state = 453
                        self.exp3()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 454
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 455
                        self.match(BKITParser.F_DIV)
                        self.state = 456
                        self.exp3()
                        pass

             
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = BKITParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_exp3)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(BKITParser.NOT)
                self.state = 463
                self.exp3()
                pass
            elif token in [BKITParser.BOOL_LIT, BKITParser.ID, BKITParser.SUB, BKITParser.F_SUB, BKITParser.LP, BKITParser.LB, BKITParser.INT_HEXA, BKITParser.INT_OCTO, BKITParser.INT_DECE, BKITParser.FLOAT_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.exp4()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def F_SUB(self):
            return self.getToken(BKITParser.F_SUB, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_exp4)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(BKITParser.SUB)
                self.state = 468
                self.exp4()
                pass
            elif token in [BKITParser.F_SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.match(BKITParser.F_SUB)
                self.state = 470
                self.exp4()
                pass
            elif token in [BKITParser.BOOL_LIT, BKITParser.ID, BKITParser.LP, BKITParser.LB, BKITParser.INT_HEXA, BKITParser.INT_OCTO, BKITParser.INT_DECE, BKITParser.FLOAT_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.exp5(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def dimensions(self):
            return self.getTypedRuleContext(BKITParser.DimensionsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 477
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 478
                    self.dimensions() 
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(BKITParser.Int_litContext,0)


        def float_lit(self):
            return self.getTypedRuleContext(BKITParser.Float_litContext,0)


        def bool_lit(self):
            return self.getTypedRuleContext(BKITParser.Bool_litContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def string_lit(self):
            return self.getTypedRuleContext(BKITParser.String_litContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def relation(self):
            return self.getTypedRuleContext(BKITParser.RelationContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_exp6)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.int_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.float_lit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                self.bool_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 487
                self.array_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 488
                self.string_lit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 489
                self.match(BKITParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 490
                self.call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 491
                self.match(BKITParser.LP)
                self.state = 492
                self.relation()
                self.state = 493
                self.match(BKITParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = BKITParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_bool_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(BKITParser.BOOL_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_DECE(self):
            return self.getToken(BKITParser.INT_DECE, 0)

        def INT_HEXA(self):
            return self.getToken(BKITParser.INT_HEXA, 0)

        def INT_OCTO(self):
            return self.getToken(BKITParser.INT_OCTO, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = BKITParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.INT_HEXA - 64)) | (1 << (BKITParser.INT_OCTO - 64)) | (1 << (BKITParser.INT_DECE - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_float_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_lit" ):
                return visitor.visitFloat_lit(self)
            else:
                return visitor.visitChildren(self)




    def float_lit(self):

        localctx = BKITParser.Float_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_float_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(BKITParser.FLOAT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_string_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_lit" ):
                return visitor.visitString_lit(self)
            else:
                return visitor.visitChildren(self)




    def string_lit(self):

        localctx = BKITParser.String_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_string_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(BKITParser.STRING_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def array_lit_element(self):
            return self.getTypedRuleContext(BKITParser.Array_lit_elementContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(BKITParser.LB)
            self.state = 506
            self.array_lit_element()
            self.state = 507
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def CM(self):
            return self.getToken(BKITParser.CM, 0)

        def array_lit_element(self):
            return self.getTypedRuleContext(BKITParser.Array_lit_elementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_lit_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_element" ):
                return visitor.visitArray_lit_element(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_element(self):

        localctx = BKITParser.Array_lit_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_array_lit_element)
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.init_value()
                self.state = 510
                self.match(BKITParser.CM)
                self.state = 511
                self.array_lit_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.init_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[46] = self.logical_sempred
        self._predicates[48] = self.exp_sempred
        self._predicates[49] = self.exp2_sempred
        self._predicates[52] = self.exp5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_sempred(self, localctx:LogicalContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




