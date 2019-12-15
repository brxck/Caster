from castervoice.lib.imports import *
from castervoice.apps.vscode import Snippet, EditorSnippet


class Javascript(MergeRule):

    mapping = {
        SymbolSpecs.IF:
            EditorSnippet("if"),
        SymbolSpecs.ELSE:
            Snippet(r" else {$0}"),
        SymbolSpecs.ELSE_IF:
            Snippet(r" else if (${1:condition}) {$0}"),

        SymbolSpecs.SWITCH:
            EditorSnippet("switch"),
        SymbolSpecs.CASE:
            Snippet(r"case ${1:value}:", r"$2", r"break"),
        SymbolSpecs.BREAK:
            Text("break"),
        SymbolSpecs.DEFAULT:
            Text("default: "),

        SymbolSpecs.DO_LOOP:
            EditorSnippet("dowhile"),
        SymbolSpecs.WHILE_LOOP:
            EditorSnippet("while"),
        SymbolSpecs.FOR_LOOP:
            Snippet(
                r"for (let ${1:i} = 0; $1 ${3|<,<=,>,>=|} ${2:limit}; $1++) {$0}"),
        SymbolSpecs.FOR_EACH_LOOP:
            EditorSnippet("fre"),
        "for in loop":
            EditorSnippet("fin"),
        "for of loop":
            EditorSnippet("fof"),

        SymbolSpecs.TO_INTEGER:
            Text("parseInt()") + Key("left"),
        SymbolSpecs.TO_FLOAT:
            Text("parseFloat()") + Key("left"),
        SymbolSpecs.TO_STRING:
            Text("String()") + Key("left"),

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
            EditorSnippet("clg"),

        SymbolSpecs.IMPORT:
            EditorSnippet("imp"),

        SymbolSpecs.FUNCTION:
            EditorSnippet("function"),
        "arrow":
            EditorSnippet("anfn"),

        SymbolSpecs.CLASS:
            Text("class {}") + Key("left"),

        SymbolSpecs.NULL:
            Text("null"),

        SymbolSpecs.RETURN:
            Text("return "),

        SymbolSpecs.TRUE:
            Text("true"),
        SymbolSpecs.FALSE:
            Text("false"),

        "destruct":
            EditorSnippet("dob"),
        "destruct array":
            EditorSnippet("dar"),

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
