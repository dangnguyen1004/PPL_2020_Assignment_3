# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u0241\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\5\2\u00a8")
        buf.write("\n\2\3\3\6\3\u00ab\n\3\r\3\16\3\u00ac\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\7\4\u00b5\n\4\f\4\16\4\u00b8\13\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\7\5\u00c4\n\5\f\5\16\5\u00c7")
        buf.write("\13\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\7D\u01c7\nD\fD\16D\u01ca\13D\3")
        buf.write("D\5D\u01cd\nD\3E\3E\3E\3E\7E\u01d3\nE\fE\16E\u01d6\13")
        buf.write("E\3F\3F\3F\3F\7F\u01dc\nF\fF\16F\u01df\13F\3G\6G\u01e2")
        buf.write("\nG\rG\16G\u01e3\3G\3G\5G\u01e8\nG\3G\5G\u01eb\nG\3H\3")
        buf.write("H\7H\u01ef\nH\fH\16H\u01f2\13H\3I\3I\3I\5I\u01f7\nI\3")
        buf.write("I\6I\u01fa\nI\rI\16I\u01fb\3J\3J\3K\3K\3L\3L\3M\3M\3N")
        buf.write("\3N\3N\3N\3N\3N\7N\u020c\nN\fN\16N\u020f\13N\3N\3N\3N")
        buf.write("\3O\3O\3O\3O\3O\3O\7O\u021a\nO\fO\16O\u021d\13O\3O\3O")
        buf.write("\3O\3O\5O\u0223\nO\3O\3O\3P\3P\3P\3P\3P\3P\7P\u022d\n")
        buf.write("P\fP\16P\u0230\13P\3P\3P\3Q\3Q\3Q\3R\3R\3R\3R\7R\u023b")
        buf.write("\nR\fR\16R\u023e\13R\3R\3R\4\u00b6\u023c\2S\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}")
        buf.write("@\177A\u0081B\u0083C\u0085D\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("E\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("F\u009dG\u009fH\u00a1I\u00a3J\3\2\21\5\2\13\f\16\17\"")
        buf.write("\"\3\2\63;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\63")
        buf.write("9\3\2\629\4\2GGgg\3\2c|\3\2C\\\3\2\62;\t\2))^^ddhhppt")
        buf.write("tvv\6\2\f\f$$))^^\3\2$$\2\u0254\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\3\u00a7")
        buf.write("\3\2\2\2\5\u00aa\3\2\2\2\7\u00b0\3\2\2\2\t\u00be\3\2\2")
        buf.write("\2\13\u00c8\3\2\2\2\r\u00cd\3\2\2\2\17\u00d3\3\2\2\2\21")
        buf.write("\u00dc\3\2\2\2\23\u00df\3\2\2\2\25\u00e4\3\2\2\2\27\u00eb")
        buf.write("\3\2\2\2\31\u00f3\3\2\2\2\33\u00f9\3\2\2\2\35\u0100\3")
        buf.write("\2\2\2\37\u0106\3\2\2\2!\u010f\3\2\2\2#\u0113\3\2\2\2")
        buf.write("%\u011c\3\2\2\2\'\u0122\3\2\2\2)\u0125\3\2\2\2+\u012f")
        buf.write("\3\2\2\2-\u0136\3\2\2\2/\u013b\3\2\2\2\61\u0140\3\2\2")
        buf.write("\2\63\u0146\3\2\2\2\65\u014a\3\2\2\2\67\u0152\3\2\2\2")
        buf.write("9\u0158\3\2\2\2;\u0163\3\2\2\2=\u0168\3\2\2\2?\u016a\3")
        buf.write("\2\2\2A\u016c\3\2\2\2C\u016e\3\2\2\2E\u0170\3\2\2\2G\u0172")
        buf.write("\3\2\2\2I\u0174\3\2\2\2K\u0176\3\2\2\2M\u0178\3\2\2\2")
        buf.write("O\u017b\3\2\2\2Q\u017e\3\2\2\2S\u0181\3\2\2\2U\u0184\3")
        buf.write("\2\2\2W\u0186\3\2\2\2Y\u0189\3\2\2\2[\u018c\3\2\2\2]\u018f")
        buf.write("\3\2\2\2_\u0192\3\2\2\2a\u0195\3\2\2\2c\u0198\3\2\2\2")
        buf.write("e\u019b\3\2\2\2g\u019e\3\2\2\2i\u01a2\3\2\2\2k\u01a6\3")
        buf.write("\2\2\2m\u01aa\3\2\2\2o\u01ac\3\2\2\2q\u01ae\3\2\2\2s\u01b0")
        buf.write("\3\2\2\2u\u01b2\3\2\2\2w\u01b4\3\2\2\2y\u01b6\3\2\2\2")
        buf.write("{\u01b8\3\2\2\2}\u01ba\3\2\2\2\177\u01bc\3\2\2\2\u0081")
        buf.write("\u01be\3\2\2\2\u0083\u01c0\3\2\2\2\u0085\u01c2\3\2\2\2")
        buf.write("\u0087\u01cc\3\2\2\2\u0089\u01ce\3\2\2\2\u008b\u01d7\3")
        buf.write("\2\2\2\u008d\u01e1\3\2\2\2\u008f\u01ec\3\2\2\2\u0091\u01f3")
        buf.write("\3\2\2\2\u0093\u01fd\3\2\2\2\u0095\u01ff\3\2\2\2\u0097")
        buf.write("\u0201\3\2\2\2\u0099\u0203\3\2\2\2\u009b\u0205\3\2\2\2")
        buf.write("\u009d\u0213\3\2\2\2\u009f\u0226\3\2\2\2\u00a1\u0233\3")
        buf.write("\2\2\2\u00a3\u0236\3\2\2\2\u00a5\u00a8\5/\30\2\u00a6\u00a8")
        buf.write("\5%\23\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\4\3\2\2\2\u00a9\u00ab\t\2\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\u00af\b\3\2\2\u00af\6\3\2\2")
        buf.write("\2\u00b0\u00b1\7,\2\2\u00b1\u00b2\7,\2\2\u00b2\u00b6\3")
        buf.write("\2\2\2\u00b3\u00b5\13\2\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b8\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b7\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ba\7")
        buf.write(",\2\2\u00ba\u00bb\7,\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd")
        buf.write("\b\4\2\2\u00bd\b\3\2\2\2\u00be\u00c5\5\u0093J\2\u00bf")
        buf.write("\u00c4\5\u0093J\2\u00c0\u00c4\5\u0095K\2\u00c1\u00c4\5")
        buf.write("\u0097L\2\u00c2\u00c4\5\u0099M\2\u00c3\u00bf\3\2\2\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2")
        buf.write("\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3")
        buf.write("\2\2\2\u00c6\n\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9")
        buf.write("\7D\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc")
        buf.write("\7{\2\2\u00cc\f\3\2\2\2\u00cd\u00ce\7D\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7m\2\2\u00d2\16\3\2\2\2\u00d3\u00d4\7E\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7w\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\20\3\2\2\2\u00dc\u00dd\7F\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\22\3\2\2\2\u00df\u00e0\7G\2\2\u00e0\u00e1")
        buf.write("\7n\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\24")
        buf.write("\3\2\2\2\u00e4\u00e5\7G\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7K\2\2\u00e9\u00ea")
        buf.write("\7h\2\2\u00ea\26\3\2\2\2\u00eb\u00ec\7G\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7f\2\2\u00ee\u00ef\7D\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7f\2\2\u00f1\u00f2\7{\2\2\u00f2\30")
        buf.write("\3\2\2\2\u00f3\u00f4\7G\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7f\2\2\u00f6\u00f7\7K\2\2\u00f7\u00f8\7h\2\2\u00f8\32")
        buf.write("\3\2\2\2\u00f9\u00fa\7G\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7f\2\2\u00fc\u00fd\7H\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7t\2\2\u00ff\34\3\2\2\2\u0100\u0101\7G\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7f\2\2\u0103\u0104\7F\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105\36\3\2\2\2\u0106\u0107\7G\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7f\2\2\u0109\u010a\7Y\2\2\u010a\u010b")
        buf.write("\7j\2\2\u010b\u010c\7k\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e \3\2\2\2\u010f\u0110\7H\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7t\2\2\u0112\"\3\2\2\2\u0113\u0114")
        buf.write("\7H\2\2\u0114\u0115\7w\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7e\2\2\u0117\u0118\7v\2\2\u0118\u0119\7k\2\2\u0119\u011a")
        buf.write("\7q\2\2\u011a\u011b\7p\2\2\u011b$\3\2\2\2\u011c\u011d")
        buf.write("\7H\2\2\u011d\u011e\7c\2\2\u011e\u011f\7n\2\2\u011f\u0120")
        buf.write("\7u\2\2\u0120\u0121\7g\2\2\u0121&\3\2\2\2\u0122\u0123")
        buf.write("\7K\2\2\u0123\u0124\7h\2\2\u0124(\3\2\2\2\u0125\u0126")
        buf.write("\7R\2\2\u0126\u0127\7c\2\2\u0127\u0128\7t\2\2\u0128\u0129")
        buf.write("\7c\2\2\u0129\u012a\7o\2\2\u012a\u012b\7g\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c\u012d\7g\2\2\u012d\u012e\7t\2\2\u012e*\3")
        buf.write("\2\2\2\u012f\u0130\7T\2\2\u0130\u0131\7g\2\2\u0131\u0132")
        buf.write("\7v\2\2\u0132\u0133\7w\2\2\u0133\u0134\7t\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135,\3\2\2\2\u0136\u0137\7V\2\2\u0137\u0138")
        buf.write("\7j\2\2\u0138\u0139\7g\2\2\u0139\u013a\7p\2\2\u013a.\3")
        buf.write("\2\2\2\u013b\u013c\7V\2\2\u013c\u013d\7t\2\2\u013d\u013e")
        buf.write("\7w\2\2\u013e\u013f\7g\2\2\u013f\60\3\2\2\2\u0140\u0141")
        buf.write("\7Y\2\2\u0141\u0142\7j\2\2\u0142\u0143\7k\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144\u0145\7g\2\2\u0145\62\3\2\2\2\u0146\u0147")
        buf.write("\7X\2\2\u0147\u0148\7c\2\2\u0148\u0149\7t\2\2\u0149\64")
        buf.write("\3\2\2\2\u014a\u014b\7r\2\2\u014b\u014c\7t\2\2\u014c\u014d")
        buf.write("\7k\2\2\u014d\u014e\7p\2\2\u014e\u014f\7v\2\2\u014f\u0150")
        buf.write("\7N\2\2\u0150\u0151\7p\2\2\u0151\66\3\2\2\2\u0152\u0153")
        buf.write("\7r\2\2\u0153\u0154\7t\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156\u0157\7v\2\2\u01578\3\2\2\2\u0158\u0159")
        buf.write("\7r\2\2\u0159\u015a\7t\2\2\u015a\u015b\7k\2\2\u015b\u015c")
        buf.write("\7p\2\2\u015c\u015d\7v\2\2\u015d\u015e\7U\2\2\u015e\u015f")
        buf.write("\7v\2\2\u015f\u0160\7t\2\2\u0160\u0161\7N\2\2\u0161\u0162")
        buf.write("\7p\2\2\u0162:\3\2\2\2\u0163\u0164\7t\2\2\u0164\u0165")
        buf.write("\7g\2\2\u0165\u0166\7c\2\2\u0166\u0167\7f\2\2\u0167<\3")
        buf.write("\2\2\2\u0168\u0169\7-\2\2\u0169>\3\2\2\2\u016a\u016b\7")
        buf.write("/\2\2\u016b@\3\2\2\2\u016c\u016d\7,\2\2\u016dB\3\2\2\2")
        buf.write("\u016e\u016f\7^\2\2\u016fD\3\2\2\2\u0170\u0171\7\'\2\2")
        buf.write("\u0171F\3\2\2\2\u0172\u0173\7?\2\2\u0173H\3\2\2\2\u0174")
        buf.write("\u0175\7>\2\2\u0175J\3\2\2\2\u0176\u0177\7@\2\2\u0177")
        buf.write("L\3\2\2\2\u0178\u0179\7>\2\2\u0179\u017a\7?\2\2\u017a")
        buf.write("N\3\2\2\2\u017b\u017c\7@\2\2\u017c\u017d\7?\2\2\u017d")
        buf.write("P\3\2\2\2\u017e\u017f\7#\2\2\u017f\u0180\7?\2\2\u0180")
        buf.write("R\3\2\2\2\u0181\u0182\7?\2\2\u0182\u0183\7?\2\2\u0183")
        buf.write("T\3\2\2\2\u0184\u0185\7#\2\2\u0185V\3\2\2\2\u0186\u0187")
        buf.write("\7(\2\2\u0187\u0188\7(\2\2\u0188X\3\2\2\2\u0189\u018a")
        buf.write("\7~\2\2\u018a\u018b\7~\2\2\u018bZ\3\2\2\2\u018c\u018d")
        buf.write("\7-\2\2\u018d\u018e\7\60\2\2\u018e\\\3\2\2\2\u018f\u0190")
        buf.write("\7/\2\2\u0190\u0191\7\60\2\2\u0191^\3\2\2\2\u0192\u0193")
        buf.write("\7,\2\2\u0193\u0194\7\60\2\2\u0194`\3\2\2\2\u0195\u0196")
        buf.write("\7^\2\2\u0196\u0197\7\60\2\2\u0197b\3\2\2\2\u0198\u0199")
        buf.write("\7>\2\2\u0199\u019a\7\60\2\2\u019ad\3\2\2\2\u019b\u019c")
        buf.write("\7@\2\2\u019c\u019d\7\60\2\2\u019df\3\2\2\2\u019e\u019f")
        buf.write("\7>\2\2\u019f\u01a0\7?\2\2\u01a0\u01a1\7\60\2\2\u01a1")
        buf.write("h\3\2\2\2\u01a2\u01a3\7@\2\2\u01a3\u01a4\7?\2\2\u01a4")
        buf.write("\u01a5\7\60\2\2\u01a5j\3\2\2\2\u01a6\u01a7\7?\2\2\u01a7")
        buf.write("\u01a8\7\61\2\2\u01a8\u01a9\7?\2\2\u01a9l\3\2\2\2\u01aa")
        buf.write("\u01ab\7*\2\2\u01abn\3\2\2\2\u01ac\u01ad\7+\2\2\u01ad")
        buf.write("p\3\2\2\2\u01ae\u01af\7}\2\2\u01afr\3\2\2\2\u01b0\u01b1")
        buf.write("\7\177\2\2\u01b1t\3\2\2\2\u01b2\u01b3\7]\2\2\u01b3v\3")
        buf.write("\2\2\2\u01b4\u01b5\7_\2\2\u01b5x\3\2\2\2\u01b6\u01b7\7")
        buf.write("<\2\2\u01b7z\3\2\2\2\u01b8\u01b9\7.\2\2\u01b9|\3\2\2\2")
        buf.write("\u01ba\u01bb\7\60\2\2\u01bb~\3\2\2\2\u01bc\u01bd\7=\2")
        buf.write("\2\u01bd\u0080\3\2\2\2\u01be\u01bf\5\u0089E\2\u01bf\u0082")
        buf.write("\3\2\2\2\u01c0\u01c1\5\u008bF\2\u01c1\u0084\3\2\2\2\u01c2")
        buf.write("\u01c3\5\u0087D\2\u01c3\u0086\3\2\2\2\u01c4\u01c8\t\3")
        buf.write("\2\2\u01c5\u01c7\5\u0099M\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01cd\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cd\7")
        buf.write("\62\2\2\u01cc\u01c4\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("\u0088\3\2\2\2\u01ce\u01cf\7\62\2\2\u01cf\u01d0\t\4\2")
        buf.write("\2\u01d0\u01d4\t\5\2\2\u01d1\u01d3\t\6\2\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u008a\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d7\u01d8\7\62\2\2\u01d8\u01d9\t\7\2\2\u01d9\u01dd")
        buf.write("\t\b\2\2\u01da\u01dc\t\t\2\2\u01db\u01da\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u008c\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e2\5")
        buf.write("\u0099M\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01ea\3\2\2\2")
        buf.write("\u01e5\u01e7\5\u008fH\2\u01e6\u01e8\5\u0091I\2\u01e7\u01e6")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01eb\5\u0091I\2\u01ea\u01e5\3\2\2\2\u01ea\u01e9\3\2")
        buf.write("\2\2\u01eb\u008e\3\2\2\2\u01ec\u01f0\5}?\2\u01ed\u01ef")
        buf.write("\5\u0099M\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u0090\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f6\t\n\2\2\u01f4\u01f7\5")
        buf.write("=\37\2\u01f5\u01f7\5? \2\u01f6\u01f4\3\2\2\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8")
        buf.write("\u01fa\5\u0099M\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2")
        buf.write("\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u0092")
        buf.write("\3\2\2\2\u01fd\u01fe\t\13\2\2\u01fe\u0094\3\2\2\2\u01ff")
        buf.write("\u0200\t\f\2\2\u0200\u0096\3\2\2\2\u0201\u0202\7a\2\2")
        buf.write("\u0202\u0098\3\2\2\2\u0203\u0204\t\r\2\2\u0204\u009a\3")
        buf.write("\2\2\2\u0205\u020d\7$\2\2\u0206\u0207\7)\2\2\u0207\u020c")
        buf.write("\7$\2\2\u0208\u0209\7^\2\2\u0209\u020c\t\16\2\2\u020a")
        buf.write("\u020c\n\17\2\2\u020b\u0206\3\2\2\2\u020b\u0208\3\2\2")
        buf.write("\2\u020b\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b")
        buf.write("\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f")
        buf.write("\u020d\3\2\2\2\u0210\u0211\7$\2\2\u0211\u0212\bN\3\2\u0212")
        buf.write("\u009c\3\2\2\2\u0213\u021b\7$\2\2\u0214\u0215\7)\2\2\u0215")
        buf.write("\u021a\7$\2\2\u0216\u0217\7^\2\2\u0217\u021a\t\16\2\2")
        buf.write("\u0218\u021a\n\17\2\2\u0219\u0214\3\2\2\2\u0219\u0216")
        buf.write("\3\2\2\2\u0219\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b")
        buf.write("\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u0222\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021e\u021f\7^\2\2\u021f\u0223\n")
        buf.write("\16\2\2\u0220\u0221\7)\2\2\u0221\u0223\n\20\2\2\u0222")
        buf.write("\u021e\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0224\3\2\2\2")
        buf.write("\u0224\u0225\bO\4\2\u0225\u009e\3\2\2\2\u0226\u022e\7")
        buf.write("$\2\2\u0227\u0228\7)\2\2\u0228\u022d\7$\2\2\u0229\u022a")
        buf.write("\7^\2\2\u022a\u022d\t\16\2\2\u022b\u022d\n\17\2\2\u022c")
        buf.write("\u0227\3\2\2\2\u022c\u0229\3\2\2\2\u022c\u022b\3\2\2\2")
        buf.write("\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3")
        buf.write("\2\2\2\u022f\u0231\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232")
        buf.write("\bP\5\2\u0232\u00a0\3\2\2\2\u0233\u0234\13\2\2\2\u0234")
        buf.write("\u0235\bQ\6\2\u0235\u00a2\3\2\2\2\u0236\u0237\7,\2\2\u0237")
        buf.write("\u0238\7,\2\2\u0238\u023c\3\2\2\2\u0239\u023b\13\2\2\2")
        buf.write("\u023a\u0239\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023c\u023a\3\2\2\2\u023d\u023f\3\2\2\2\u023e\u023c")
        buf.write("\3\2\2\2\u023f\u0240\bR\7\2\u0240\u00a4\3\2\2\2\32\2\u00a7")
        buf.write("\u00ac\u00b6\u00c3\u00c5\u01c8\u01cc\u01d4\u01dd\u01e3")
        buf.write("\u01e7\u01ea\u01f0\u01f6\u01fb\u020b\u020d\u0219\u021b")
        buf.write("\u0222\u022c\u022e\u023c\b\b\2\2\3N\2\3O\3\3P\4\3Q\5\3")
        buf.write("R\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL_LIT = 1
    WS = 2
    CMT = 3
    ID = 4
    BODY = 5
    BREAK = 6
    CONTINUE = 7
    DO = 8
    ELSE = 9
    ELSEIF = 10
    ENDBODY = 11
    ENDIF = 12
    ENDFOR = 13
    ENDDO = 14
    ENDWHILE = 15
    FOR = 16
    FUNCTION = 17
    FALSE = 18
    IF = 19
    PARAMETER = 20
    RETURN = 21
    THEN = 22
    TRUE = 23
    WHILE = 24
    VAR = 25
    PRINTLN = 26
    PRINT = 27
    PRINTSTRLN = 28
    READ = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    EQ = 35
    LESS = 36
    GREATER = 37
    LESS_EQ = 38
    GREATER_EQ = 39
    NOT_EQ = 40
    EQ_RELATION = 41
    NOT = 42
    AND = 43
    OR = 44
    F_ADD = 45
    F_SUB = 46
    F_MUL = 47
    F_DIV = 48
    F_LESS = 49
    F_GREATER = 50
    F_LESS_EQ = 51
    F_GREATER_EQ = 52
    F_NOT_EQ = 53
    LP = 54
    RP = 55
    LB = 56
    RB = 57
    LSB = 58
    RSB = 59
    COLON = 60
    CM = 61
    DOT = 62
    SM = 63
    INT_HEXA = 64
    INT_OCTO = 65
    INT_DECE = 66
    FLOAT_LIT = 67
    STRING_LIT = 68
    ILLEGAL_ESCAPE = 69
    UNCLOSE_STRING = 70
    ERROR_CHAR = 71
    UNTERMINATED_COMMENT = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndDo'", "'EndWhile'", 
            "'For'", "'Function'", "'False'", "'If'", "'Parameter'", "'Return'", 
            "'Then'", "'True'", "'While'", "'Var'", "'printLn'", "'print'", 
            "'printStrLn'", "'read'", "'+'", "'-'", "'*'", "'\\'", "'%'", 
            "'='", "'<'", "'>'", "'<='", "'>='", "'!='", "'=='", "'!'", 
            "'&&'", "'||'", "'+.'", "'-.'", "'*.'", "'\\.'", "'<.'", "'>.'", 
            "'<=.'", "'>=.'", "'=/='", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "':'", "','", "'.'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL_LIT", "WS", "CMT", "ID", "BODY", "BREAK", "CONTINUE", 
            "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDDO", 
            "ENDWHILE", "FOR", "FUNCTION", "FALSE", "IF", "PARAMETER", "RETURN", 
            "THEN", "TRUE", "WHILE", "VAR", "PRINTLN", "PRINT", "PRINTSTRLN", 
            "READ", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "LESS", "GREATER", 
            "LESS_EQ", "GREATER_EQ", "NOT_EQ", "EQ_RELATION", "NOT", "AND", 
            "OR", "F_ADD", "F_SUB", "F_MUL", "F_DIV", "F_LESS", "F_GREATER", 
            "F_LESS_EQ", "F_GREATER_EQ", "F_NOT_EQ", "LP", "RP", "LB", "RB", 
            "LSB", "RSB", "COLON", "CM", "DOT", "SM", "INT_HEXA", "INT_OCTO", 
            "INT_DECE", "FLOAT_LIT", "STRING_LIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "BOOL_LIT", "WS", "CMT", "ID", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDDO", "ENDWHILE", "FOR", "FUNCTION", "FALSE", "IF", 
                  "PARAMETER", "RETURN", "THEN", "TRUE", "WHILE", "VAR", 
                  "PRINTLN", "PRINT", "PRINTSTRLN", "READ", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "EQ", "LESS", "GREATER", "LESS_EQ", 
                  "GREATER_EQ", "NOT_EQ", "EQ_RELATION", "NOT", "AND", "OR", 
                  "F_ADD", "F_SUB", "F_MUL", "F_DIV", "F_LESS", "F_GREATER", 
                  "F_LESS_EQ", "F_GREATER_EQ", "F_NOT_EQ", "LP", "RP", "LB", 
                  "RB", "LSB", "RSB", "COLON", "CM", "DOT", "SM", "INT_HEXA", 
                  "INT_OCTO", "INT_DECE", "INT_DEC", "INT_HEX", "INT_OCT", 
                  "FLOAT_LIT", "FLOAT_DEC_PART", "FLOAT_EXP_PART", "LOWER", 
                  "UPPER", "UNDERSCORES", "DIGITS", "STRING_LIT", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[76] = self.STRING_LIT_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.UNCLOSE_STRING_action 
            actions[79] = self.ERROR_CHAR_action 
            actions[80] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                            self.text = self.text[1:-1]
                        
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                                raise IllegalEscape(self.text[1:])
                            
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                                raise UncloseString(self.text[1:])
                            
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                                raise ErrorToken(self.text)
                            
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                                raise UnterminatedComment()
                            
     


