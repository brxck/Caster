'''
Created on Sep 1, 2015

@author: synkarius
'''
from castervoice.lib.imports import *
from castervoice.lib.ccr.standard import SymbolSpecs
from castervoice.lib.ccr.core.punctuation import text_punc_dict
from castervoice.lib.alphanumeric import caster_alphabet

_NEXUS = control.nexus()


class Navigation(MergeRule):
    pronunciation = CCRMerger.CORE[1]

    mapping = {
        "clipboard erase":
        R(Function(navigation.erase_multi_clipboard, nexus=_NEXUS)),

        "find next [<nnavi10>]":
            R(Key("f3"))*Repeat(extra="nnavi10"),
        "find prior [<nnavi10>]":
            R(Key("s-f3"))*Repeat(extra="nnavi10"),

        "context menu":
            R(Key("s-f10")),

        "grab [<nnavi10>]":
            R(Mouse("left") + Mouse("left") + Function(
                navigation.stoosh_keep_clipboard,
                nexus=_NEXUS)),
        "drop [<nnavi10>]":
            R(Mouse("left") + Mouse("left") + Function(
                navigation.drop_keep_clipboard,
                nexus=_NEXUS,
                capitalization=0,
                spacing=0)),

        "refresh":
            R(Key("c-r")),

        # Window Management
        "window up":
            R(Key("w-up")),
        "window down":
            R(Key("w-down")),
        "window left [<nnavi10>]":
            R(Key("w-left"))*Repeat(extra="nnavi10"),
        "window right [<nnavi10>]":
            R(Key("w-right"))*Repeat(extra="nnavi10"),
        "monitor left [<nnavi10>]":
            R(Key("sw-left"))*Repeat(extra="nnavi10"),
        "monitor right [<nnavi10>]":
            R(Key("sw-right"))*Repeat(extra="nnavi10"),

        # Rofi: switching and launching
        "launch [<textnv>]":
            R(Key("w-r") + Pause("10") + Text("%(textnv)s")),
        "switch [<textnv>]":
            R(Key("w-w") + Pause("10") + Text("%(textnv)s")),
        "rofi [<textnv>]":
            R(Key("w-e") + Pause("10") + Text("%(textnv)s")),

        # Workspace management
        "work down [<nnavi10>]":
            R(Key("w-pgdown"))*Repeat(extra="nnavi10"),
        "work up [<nnavi10>]":
            R(Key("w-pgup"))*Repeat(extra="nnavi10"),
        "send down [<nnavi10>]":
            R(Key("ws-pgdown"))*Repeat(extra="nnavi10"),
        "send up [<nnavi10>]":
            R(Key("ws-pgup"))*Repeat(extra="nnavi10"),
        "work <nnavi10>":
            R(Key("w-%(nnavi10)d")),
        "send <nnavi10>":
            R(Key("sw-%(nnavi10)d")),

        "nexta [<nnavi10>]":
            R(Key("c-pgdown"))*Repeat(extra="nnavi10"),
        "prexta [<nnavi10>]":
            R(Key("c-pgup"))*Repeat(extra="nnavi10"),
        "tab close [<nnavi10>]":
            R(Key("c-w/20"))*Repeat(extra="nnavi10"),
        "tab restore":
            R(Key("cs-t")),
        "quake":
            R(Key("w-q")),
        "find":
            R(Key("c-f")),

        # keyboard shortcuts
        "meta [<textnv>]":
            R(Key("win/200") + Text("%(textnv)s")),
        "save":
            R(Key("c-s")),
        "shock [<nnavi50>]":
            R(Key("tab")) * Repeat(extra="nnavi50"),
        "slap [<nnavi50>]":
            R(Key("enter")) * Repeat(extra="nnavi50"),
        "slide [<nnavi50>]":
            R(Key("end, enter")) * Repeat(extra="nnavi50"),
        "slip [<nnavi50>]":
            R(Key("home, enter, up")) * Repeat(extra="nnavi50"),

        "select all":
            R(Key("c-a")),
        "shift click":
            R(Key("shift:down") + Mouse("left") + Key("shift:up")),
        "copy [<nnavi500>]":
            R(Function(navigation.stoosh_keep_clipboard, nexus=_NEXUS)),
        "cut [<nnavi500>]":
            R(Function(navigation.cut_keep_clipboard, nexus=_NEXUS)),
        "spark [<nnavi500>] [(<capitalization> <spacing> | <capitalization> | <spacing>) [(bow|bowel)]]":
            R(Function(navigation.drop_keep_clipboard, nexus=_NEXUS)),
        "whack [<splatdir>] [<nnavi10>]":
            R(Key("c-%(splatdir)s")) * Repeat(extra="nnavi10"),
        "bump [<nnavi10>]":
            R(Key("c-delete")) * Repeat(extra="nnavi10"),
        "chuck [<nnavi50>]":
            R(Key("del/5")) * Repeat(extra="nnavi50"),
        "scratch [<nnavi50>]":
            R(Key("backspace/5:%(nnavi50)d")),
        SymbolSpecs.CANCEL:
            R(Key("escape")),
        "shackle":
            R(Key("home/5, s-end")),
        "duple [<nnavi50>]":
            R(Function(navigation.duple_keep_clipboard)),
        "Kraken":
            R(Key("c-space")),
        "undo [<nnavi10>]":
            R(Key("c-z"))*Repeat(extra="nnavi10"),
        "redo [<nnavi10>]":
            R(
                ContextAction(default=Key("c-y")*Repeat(extra="nnavi10"),
                              actions=[
                                  (AppContext(executable=["rstudio", "foxitreader"]),
                                   Key("cs-z")*Repeat(extra="nnavi10")),
                ])),

        # text formatting
        "set [<big>] format (<capitalization> <spacing> | <capitalization> | <spacing>) [(bow|bowel)]":
            R(Function(textformat.set_text_format)),
        "clear [<big>] formatting":
            R(Function(textformat.clear_text_format)),
        "peek [<big>] format":
            R(Function(textformat.peek_text_format)),
        "(<capitalization> <spacing> | <capitalization> | <spacing>) [(bow|bowel)] <textnv> [brunt]":
            R(Function(textformat.master_format_text)),
        "[<big>] format <textnv>":
            R(Function(textformat.prior_text_format)),
        "<word_limit> [<big>] format <textnv>":
            R(Function(textformat.partial_format_text)),
        "nope":
            R(Function(textformat.delete_last_text)),
        "that was (<capitalization> <spacing> | <capitalization> | <spacing>) [(bow|bowel)]":
            R(Function(textformat.reformat_last_text)),

        # Window Switching
        "flip [<textnv>]":
            R(Key("w-e") + Text("%(textnv)s")),
        "launch [<textnv>]":
            R(Key("w-r") + Text("%(textnv)s")),

        # Mouse Commands
        "kick [<nnavi3>]":
            R(Function(navigation.left_click, nexus=_NEXUS)) * \
        Repeat(extra="nnavi3"),
        "psychic":
            R(Function(navigation.right_click, nexus=_NEXUS)),
        "mid kick":
            R(Function(navigation.middle_click, nexus=_NEXUS)),
        "squat":
            R(Function(navigation.left_down, nexus=_NEXUS)),
        "bench":
            R(Function(navigation.left_up, nexus=_NEXUS)),

        # Keystroke Commands
        "<direction> [<nnavi500>]":
            R(Key("%(direction)s") * Repeat(extra='nnavi500')),
        "strike [<nnavi10>]":
            R(Key("home:%(nnavi10)s")),
        "struck [<nnavi10>]":
            R(Key("end:%(nnavi10)s")),
        "strike out [<nnavi10>]":
            R(Key("c-home:%(nnavi10)s")),
        "struck out [<nnavi10>]":
            R(Key("c-end:%(nnavi10)s")),
        "strike select [<nnavi10>]":
            R(Key("s-home:%(nnavi10)s")),
        "struck select [<nnavi10>]":
            R(Key("s-end:%(nnavi10)s")),
        "lore [<nnavi500>]":
            R(Key("c-left:%(nnavi500)s")),
        "role [<nnavi500>]":
            R(Key("c-right:%(nnavi500)s")),
        "lorick [<nnavi500>]":
            R(Key("s-left:%(nnavi500)s")),
        "rolick [<nnavi500>]":
            R(Key("s-right:%(nnavi500)s")),
        "lorex [<nnavi500>]":
            R(Key("cs-left:%(nnavi500)s")),
        "rolex [<nnavi500>]":
            R(Key("cs-right:%(nnavi500)s")),

        "punch [<nnavi10>]":
            R(Key("pagedown:%(nnavi10)s")),
        "pinch [<nnavi10>]":
            R(Key("pageup:%(nnavi10)s")),
    }

    modifier_choice_object = Choice("modifier", {
        "(control | fly)": "c-",  # TODO: make DRY
        "(shift | shin)": "s-",
        "alt": "a-",
        "(control shift | que)": "cs-",
        "control alt": "ca-",
        "(shift alt | alt shift)": "sa-",
        "(control alt shift | control shift alt)": "csa-",  # control must go first
        "windows": "w-",  # windows should go before alt/shift
        "control windows": "cw-",
        "control windows alt": "cwa-",
        "control windows shift": "cws-",
        "windows shift alt": "wsa-",
        "windows alt shift": "was-",
        "windows shift": "ws-",
        "windows alt": "wa-",
        "control windows alt shift": "cwas-",
        "hit": "",
    })

    # I tried to limit which things get repeated how many times in hopes that it will help prevent the bad grammar error
    # this could definitely be changed. perhaps some of these should be made non-CCR
    button_dictionary_500 = {"(tab | tabby)": "tab", "(backspace | clear)": "backspace", "(delete|deli)": "del", "(escape | cancel)": "escape", "(enter | shock)": "enter",
                             "(left | lease)": "left", "(right | ross)": "right", "(up | sauce)": "up",
                             "(down | dunce)": "down", "page (down | dunce)": "pagedown", "page (up | sauce)": "pageup", "space": "space"}
    button_dictionary_10 = {"function {}".format(
        i): "f{}".format(i) for i in range(1, 10)}
    button_dictionary_10.update(caster_alphabet)
    button_dictionary_10.update(text_punc_dict)
    longhand_punctuation_names = {"minus": "hyphen", "hyphen": "hyphen", "comma": "comma",
                                  "deckle": "colon", "colon": "colon", "slash": "slash", "backslash": "backslash"}
    button_dictionary_10.update(longhand_punctuation_names)
    button_dictionary_1 = {"(home | lease wally | latch)": "home", "(end | ross wally | ratch)": "end", "insert": "insert", "zero": "0",
                           "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    combined_button_dictionary = {}
    for dictionary in [button_dictionary_1, button_dictionary_10, button_dictionary_500]:
        combined_button_dictionary.update(dictionary)

    extras = [
        IntegerRefST("nnavi10", 1, 11),
        IntegerRefST("nnavi3", 1, 4),
        IntegerRefST("nnavi50", 1, 50),
        IntegerRefST("nnavi500", 1, 500),
        Dictation("textnv"),
        Choice("direction", {
            "dunce": "down",
            "sauce": "up",
            "lease": "left",
            "ross": "right",
        }),
        Choice("capitalization", {
            "yell": 1,
            "tie": 2,
            "camel": 3,
            "speak": 4,
            "say": 5
        }),
        Choice(
            "spacing", {
                "gum": 1,
                "gun": 1,
                "spine": 2,
                "snake": 3,
                "pebble": 4,
                "incline": 5,
                "dissent": 6,
                "descent": 6
            }),
        Choice("word_limit", {
            "single": 1,
            "double": 2,
            "triple": 3,
            "Quadra": 4
        }),
        navigation.TARGET_CHOICE,
        navigation.get_direction_choice("mtn_dir"),
        Choice("mtn_mode", {
            "shin": "s",
            "queue": "cs",
            "fly": "c",
        }),
        Choice("extreme", {
            "end": "way",
        }),
        Choice("big", {
            "big": True,
        }),
        Choice("splatdir", {
            "lease": "backspace",
            "ross": "delete",
        }),
    ]

    defaults = {
        "nnavi500": 1,
        "nnavi50": 1,
        "nnavi10": 1,
        "nnavi3": 1,
        "textnv": "",
        "capitalization": 0,
        "spacing": 0,
        "mtn_mode": None,
        "mtn_dir": "right",
        "extreme": None,
        "big": False,
        "splatdir": "backspace",
        "modifier": "",
    }


control.global_rule(Navigation())
