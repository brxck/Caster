from castervoice.lib.imports import *
from castervoice.apps.vscode import Snippet, EditorSnippet


class Python(MergeRule):

    mapping = {
        SymbolSpecs.IF:
            EditorSnippet("if"),
        SymbolSpecs.ELSE:
            EditorSnippet("else"),
        SymbolSpecs.ELSE_IF:
            EditorSnippet("elif"),

        SymbolSpecs.BREAK:
            Text("break"),
        "(for in loop|{}|{})".format(SymbolSpecs.FOR_EACH_LOOP, SymbolSpecs.FOR_LOOP):
            EditorSnippet("for"),
        SymbolSpecs.WHILE_LOOP:
            EditorSnippet("while"),

        SymbolSpecs.TO_INTEGER:
            Text("int()") + Key("left"),
        SymbolSpecs.TO_FLOAT:
            Text("float()") + Key("left"),
        SymbolSpecs.TO_STRING:
            Text("str()") + Key("left"),

        SymbolSpecs.AND:
            Snippet(" and "),
        SymbolSpecs.OR:
            Text(" or "),
        SymbolSpecs.NOT:
            Text("!"),

        SymbolSpecs.SYSOUT:
            Text("print()") + Key("left"),
        SymbolSpecs.IMPORT:
            Snippet(r"from ${1:package} import ${2:module}"),
        SymbolSpecs.FUNCTION:
            EditorSnippet("def"),
        SymbolSpecs.CLASS:
            EditorSnippet("class"),
        SymbolSpecs.NULL:
            Text("None"),
        SymbolSpecs.RETURN:
            Text("return "),
        SymbolSpecs.TRUE:
            Text("True"),
        SymbolSpecs.FALSE:
            Text("False"),

        "self":
            Text("self"),
        "long not":
            Text("not "),
        "long in":
            Text(" in "),
        "long is":
            Text(" is "),
        "length of":
            Snippet(r"len($1)"),
        "list (comprehension | comp)":
            Snippet(
                r"[${1:expression} for ${2:item} in ${3:list} if ${4:condition}]"),
        "dict (comprehension | comp)":
            Snippet(
                r"{${1:key} ${2:expression} for ${3:item} in ${4:list} if ${5:condition}}"),
        "dot pie":
            Text(".py"),
        "yield":
            Text("yield "),

        # class and class methods
        "dunder":
            Text("____()") + Key("left:4"),
        "init":
            Text("__init__()") + Key("left"),
    }


control.global_rule(Python(ID=100))
