from dragonfly import Choice, Repeat

from castervoice.lib import control
from castervoice.lib.actions import Key, Text
from dragonfly.actions.action_mimic import Mimic
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

text_punc_dict = {
    "slam":                                               " ",
    "bang":                                               "!",
    "quote":                                             "\"",
    "amper":                                              "&",
    "pound":                                              "#",
    "doll":                                               "$",
    "percy":                                              "%",
    "smote":                                              "'",
    "splat":                                              "*",
    "cross":                                              "+",
    "equit":                                              "=",
    "dit":                                                ",",
    "dash":                                               "-",
    "period | dot":                                       ".",
    "slash":                                              "/",
    "cat":                                                ":",
    "semi":                                               ";",
    "quell":                                              "?",
    "insta":                                              "@",
    "clash":                                             "\\",
    "carrot":                                             "^",
    "flat":                                               "_",
    "smite":                                              "`",
    "bar":                                                "|",
    "wave":                                               "~",

    "assign":                                           " = ",
    "plus":                                             " + ",
    "minus":                                            " - ",
    "divide":                                           " / ",
    "modulo":                                           " % ",
    "coy":                                               ": ",
    "drip":                                              ", ",
    "boom":                                              ". ",

    "bend":                                               "(",
    "rend":                                               ")",
    "angle":                                              "<",
    "rangle":                                             ">",
    "ace":                                                "[",
    "race":                                               "]",
    "burl":                                               "{",
    "curl":                                               "}",

    "less than":                                        " < ",
    "less equals":                                     " <= ",
    "strict equals":                                  " === ",
    "not strict equals":                              " !== ",
    "equals":                                          " == ",
    "not equals":                                      " != ",
    "greater than":                                     " > ",
    "greater equals":                                  " >= ",

    "plus equals":                                     " += ",
    "minus equals":                                    " -= ",
    "plus plus":                                        "++ ",
    "minus minus":                                      "-- ",
}


class Punctuation(MergeRule):
    pronunciation = CCRMerger.CORE[3]

    mapping = {
        "[<long>] <text_punc> [<npunc>]":
            R(Text("%(long)s" + "%(text_punc)s" + "%(long)s")) *
        Repeat(extra="npunc"),
        # For some reason, this one doesn't work through the other function
        "[<long>] backslash [<npunc>]":
            R(Text("%(long)s" + "\\" + "%(long)s"))*Repeat(extra="npunc"),
    }

    extras = [
        IntegerRefST("npunc", 0, 10),
        Choice(
            "long", {
                "long": " ",
            }),
        Choice(
            "text_punc", text_punc_dict)
    ]
    defaults = {
        "npunc": 1,
        "long": "",
    }


control.global_rule(Punctuation())
