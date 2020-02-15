'''
Created on Oct 17, 2015

@author: synkarius
'''


class SymbolSpecs(object):
    IF = "iffy"
    ELSE = "shells"
    ELSE_IF = "shells if"

    SWITCH = "switchy"
    CASE = "case of"
    BREAK = "breaker"
    DEFAULT = "defraud"

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

    IMPORT = "impose"

    FUNCTION = "func"
    LAMBDA = "lamb"
    CLASS = "grass"

    DOCSTRING = "docstring"

    RETURN = "jedi"

    NULL = "value not"
    TRUE = "value true"
    FALSE = "value false"

    # not part of the programming standard:
    CANCEL = "(terminate | escape | exit | cancel)"

    @staticmethod
    def set_cancel_word(spec):
        SymbolSpecs.CANCEL = spec
