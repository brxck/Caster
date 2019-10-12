from dragonfly import Choice, Repeat

from castervoice.lib import control
from castervoice.lib.actions import Key, Text
from dragonfly.actions.action_mimic import Mimic
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

# double_text_punc_dict = {
#     "quotes":                            "\"\"",
#     "smotes":                              "''",
#     "tickris":                             "``",
#     "parens":                              "()",
#     "brax":                                "[]",
#     "curl":                                "{}",
#     "angle":                               "<>",
# }

# inv_dtpb = {v: k for k, v in double_text_punc_dict.iteritems()}

text_punc_dict = {
    "haste":                                              " ",
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
    "drip":                                               ",",
    "dash":                                               "-",
    "period | dot":                                       ".",
    "slash":                                              "/",
    "cat":                                                ":",
    "semi":                                               ";",
    "quest":                                              "?",
    "insta":                                              "@",
    "clash":                                             "\\",
    "carrot":                                            "^",
    "flat":                                               "_",
    "quirk":                                              "`",
    "bar":                                                "|",
    "wave":                                               "~",

    "assign":                                           " = ",
    "plus":                                             " + ",
    "minus":                                            " - ",
    "divide":                                           " / ",
    "modulo":                                           " % ",
    "coy":                                               ": ",
    "bam":                                               ", ",
    "boom":                                              ". ",

    "[open] bend":                                        "(",
    "(close bend|rend)":                                  ")",
    "[open] angle":                                       "<",
    "(close angle|rangle)":                               ">",
    "[open] ace":                                         "[",
    "(close ace|race)":                                   "]",
    "[open] burl":                                        "{",
    "(close burl|curl)":                                  "}",

    "less than":                                        " < ",
    "less equals":                                     " <= ",
    "strict equals":                                  " === ",
    "not strict equals":                              " !== ",
    "equals":                                          " == ",
    "not equals":                                        "!=",
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
        # "<double_text_punc> [<npunc>]":
        #     R(Text("%(double_text_punc)s") + Key("left"))*Repeat(extra="npunc"),
        # "[<long>] pair <text_punc>":
        #     R(Text("%(text_punc)s" + "%(long)s" + "%(long)s") + \
        #       Mimic("close", "%(text_punc)s")),
        "shock [<npunc>]":
            R(Key("tab"))*Repeat(extra="npunc"),
        "(back | shin) shock [<npunc>]":
            R(Key("s-tab"))*Repeat(extra="npunc"),
        "haste [<npunc100>]":
            R(Text(" "))*Repeat(extra="npunc100"),
    }

    extras = [
        IntegerRefST("npunc", 0, 10),
        IntegerRefST("npunc100", 0, 100),
        Choice(
            "long", {
                "long": " ",
            }),
        Choice(
            "text_punc", text_punc_dict)
    ]
    defaults = {
        "npunc": 1,
        "npunc100": 1,
        "long": "",
    }


control.global_rule(Punctuation())
