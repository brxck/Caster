'''
Created on Oct 17, 2015

@author: synkarius
'''


class SymbolSpecs(object):
    IF = "iffae"
    ELSE = "shells"
    IF_ELSE = "if shells"

    SWITCH = "switchy"
    CASE = "case of"
    BREAK = "breaker"
    DEFAULT = "default"

    DO_LOOP = "do loop"
    WHILE_LOOP = "while loop"
    FOR_LOOP = "for loop"
    FOR_EACH_LOOP = "for each"

    REDUCE = "op reduce"
    MAP = "op map"
    FILTER = "op filter"

    TO_INTEGER = "to int"
    TO_FLOAT = "to float"
    TO_STRING = "to string"

    AND = "lodge and"
    OR = "lodge or"
    NOT = "lodge not"

    SYSOUT = "sysout"

    IMPORT = "import"

    FUNCTION = "func"
    LAMBDA = "lam"
    CLASS = "class"

    DOCSTRING = "docstring"

    RETURN = "return"

    NULL = "value not"
    TRUE = "value true"
    FALSE = "value false"

    # not part of the programming standard:
    CANCEL = "(terminate | escape | exit | cancel)"

    @staticmethod
    def set_cancel_word(spec):
        SymbolSpecs.CANCEL = spec
