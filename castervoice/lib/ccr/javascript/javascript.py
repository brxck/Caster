'''
Created on Sep 2, 2015

@author: synkarius
'''
from castervoice.lib.imports import *


def Snippet(prefix):
        return Text(prefix) + Pause("50") + Key("tab")


class Javascript(MergeRule):

    mapping = {
        SymbolSpecs.IF:
            Snippet("if"),
        SymbolSpecs.ELSE:
            Snippet("ifelse"),

        SymbolSpecs.SWITCH:
            Snippet("switch"),
        SymbolSpecs.CASE:
            Text("case :") + Key("left")),
        SymbolSpecs.BREAK:
            Text("break"),
        SymbolSpecs.DEFAULT:
            Text("default: "),

        SymbolSpecs.DO_LOOP:
            Snippet("dowhile"),
        SymbolSpecs.WHILE_LOOP:
            Snippet("while"),
        SymbolSpecs.FOR_LOOP:
            Snippet("for"),
        SymbolSpecs.FOR_EACH_LOOP:
            Snippet("fre"),
        "for in loop":
            Snippet("fin"),
        "for of loop":
            Snippet("fof"),

        SymbolSpecs.TO_INTEGER:
            Text("parseInt()") + Key("left"),
        SymbolSpecs.TO_FLOAT:
            Text("parseFloat()") + Key("left"),
        SymbolSpecs.TO_STRING:
            Key("dquote, dquote, plus"),

        SymbolSpecs.REDUCE:
            Text(".reduce()") + Key("left"),
        SymbolSpecs.MAP:
            Text(".map()") + Key("left"),
        SymbolSpecs.FILTER:
            Text(".filter()") + Key("left"),

        SymbolSpecs.AND:
            Text(" && "),
        SymbolSpecs.OR:
            Text(" || "),
        SymbolSpecs.NOT:
            Text("!"),

        SymbolSpecs.SYSOUT:
            Snippet("clg"),

        SymbolSpecs.IMPORT:
            Snippet("imp"),

        SymbolSpecs.FUNCTION:
            Snippet("function"),
        "arrow":
            Snippet("anfn"),

        SymbolSpecs.CLASS:
            Text("class  {}") + Key("left/5:3"),

        SymbolSpecs.NULL:
            Text("null"),

        SymbolSpecs.RETURN:
            Text("return "),

        SymbolSpecs.TRUE:
            Text("true"),
        SymbolSpecs.FALSE:
            Text("false"),

        "destruct":
            Snippet("dob"),
        "destruct array":
            Snippet("dar"),

        "this":
            Text("this"),
        "inner HTML":
            Text("innerHTML"),
        "new new":
            Text("new "),
        "throw":
            Text("throw "),
        "var":
            Text("var "),
        "const":
            Text("const "),
        "let":
            Text("let "),
        "a sink":
            Text("async "),
        "await":
            Text("await "),
    }

    extras = []
    defaults = {}


control.global_rule(Javascript(ID=200))
