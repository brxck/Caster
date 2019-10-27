'''
Created on Sep 2, 2015

@author: synkarius
'''
from castervoice.lib.imports import *


class Javascript(MergeRule):

    mapping = {

        # CCR PROGRAMMING STANDARD
        SymbolSpecs.IF:
            R(Text("if () ") + Key("left, enter, up")),
        SymbolSpecs.ELSE:
            R(Text("else {}") + Key("left, enter, up")),
        #
        SymbolSpecs.SWITCH:
            R(Text("switch () {}") + Key("left, enter, up")),
        SymbolSpecs.CASE:
            R(Text("case :") + Key("left")),
        SymbolSpecs.BREAK:
            R(Text("break")),
        SymbolSpecs.DEFAULT:
            R(Text("default: ")),
        #
        SymbolSpecs.DO_LOOP:
            R(Text("do {}") + Key("left, enter")),
        SymbolSpecs.WHILE_LOOP:
            R(Text("while ()") + Key("left")),
        SymbolSpecs.FOR_LOOP:
            R(Text("for (var i=0; i<TOKEN; i++)")),
        SymbolSpecs.FOR_EACH_LOOP:
            R(Text("for (TOKEN in TOKEN)")),
        #
        SymbolSpecs.TO_INTEGER:
            R(Text("parseInt()") + Key("left")),
        SymbolSpecs.TO_FLOAT:
            R(Text("parseFloat()") + Key("left")),
        SymbolSpecs.TO_STRING:
            R(Key("dquote, dquote, plus")),
        #
        SymbolSpecs.AND:
            R(Text(" && ")),
        SymbolSpecs.OR:
            R(Text(" || ")),
        SymbolSpecs.NOT:
            R(Text("!")),
        #
        SymbolSpecs.SYSOUT:
            R(Text("console.log()") + Key("left")),
        #
        SymbolSpecs.IMPORT:
            R(Text("import ")),
        #
        SymbolSpecs.FUNCTION:
            R(Text("function () {}") + Key("left:2, enter") +
              SelectiveAction(Key("enter, up"), ["AptanaStudio3.exe"])),
            SymbolSpecs.CLASS:
            R(Text("class  {}") + Key("left/5:3")),
        #
        SymbolSpecs.COMMENT:
            R(Text("//")),
        SymbolSpecs.LONG_COMMENT:
            R(Text("/**/") + Key("left,left")),
        #
        SymbolSpecs.NULL:
            R(Text("null")),
        #
        SymbolSpecs.RETURN:
            R(Text("return ")),
        #
        SymbolSpecs.TRUE:
            R(Text("true")),
        SymbolSpecs.FALSE:
            R(Text("false")),

        # JavaScript specific
        "arrow":
            R(Text("() => {}") + Key("left:1, enter")),
        "index of":
            R(Text("indexOf()") + Key("left")),
        "this":
            R(Text("this")),
        "inner HTML":
            R(Text("innerHTML")),
        "new new":
            R(Text("new ")),
        "throw":
            R(Text("throw ")),
        "var":
            R(Text("var ")),
        "const":
            R(Text("const ")),
        "let":
            R(Text("let ")),
        "shell iffae":
            R(Text("else if ()") + Key("left")),
        "a sink":
            R(Text("async ")),
        "await":
            R(Text("await ")),
    }

    extras = []
    defaults = {}


control.global_rule(Javascript(ID=200))
