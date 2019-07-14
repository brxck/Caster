from dragonfly import Choice, Repeat

from castervoice.lib import control
from castervoice.lib.actions import Key, Text
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
    "ace":                                                " ",
    "bang":                                               "!",
    "quote":                                             "\"",
    "ampersand":                                          "&",
    "pound":                                              "#",
    "Dolly":                                              "$",
    "percy":                                              "%",
    "smote":                                              "'",
    "splat":                                              "*",
    "cross":                                              "+",
    "equit":                                             "=",
    "drip":                                               ",",
    "dash":                                               "-",
    "period | dot":                                       ".",
    "slash":                                              "/",
    "cat":                                                ":",
    "semi":                                               ";",
    "quest":                                             "?",
    "(atty | at symbol)":                                 "@",
    "backslash":                                         "\\",
    "carrot":                                             "^",
    "flat":                                               "_",
    "ticky":                                              "`",
    "bar":                                                "|",
    "tilde":                                              "~",

    "[open] bend":                                       "(",
    "close bend":                                        ")",
    "[open] angle":                                       "<",
    "close angle":                                        ">",
    "[open] brax":                                        "[",
    "close brax":                                         "]",
    "[open] curl":                                        "{",
    "close curl":                                         "}",

    "[is] less than": " < ",
    "[is] less [than] [or] equal [to]":                " <= ",
    "strict":                                         " === ",
    "[is] equal to":                                   " == ",
    "[is] greater than":                                " > ",
    "[is] greater [than] [or] equal [to]":             " >= ",
}

class Punctuation(MergeRule):
    pronunciation = CCRMerger.CORE[3]

    mapping = {
        "[<long>] <text_punc> [<npunc>]":
            R(Text("%(long)s" + "%(text_punc)s" + "%(long)s"))*Repeat(extra="npunc"),
        # For some reason, this one doesn't work through the other function
        "[<long>] backslash [<npunc>]":
            R(Text("%(long)s" + "\\" + "%(long)s"))*Repeat(extra="npunc"),
        # "<double_text_punc> [<npunc>]":
        #     R(Text("%(double_text_punc)s") + Key("left"))*Repeat(extra="npunc"),
        "shock [<npunc>]":
            R(Key("tab"))*Repeat(extra="npunc"),
        "(back | shin) shock [<npunc>]":
            R(Key("s-tab"))*Repeat(extra="npunc"),
        "coy [<npunc>]":
            R(Text(", "))*Repeat(extra="npunc"),
        "bam [<npunc>]":
            R(Text(". "))*Repeat(extra="npunc"),
        "ace [<npunc100>]":
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
