# thanks to Casper for contributing commands to this.
from castervoice.lib.imports import *
from castervoice.lib.alphanumeric import caster_alphabet

class VSCodeNonCcrRule(MergeRule):
    pronunciation = "Visual Studio Code Non Continuous"
    mapping = {
        # Moving around a file
        "line jump <n>":
            R(Key("c-g") + Text("%(n)d") + Key("enter")),
        "[line] <action> <ln1> [by <ln2>]":
            R(Function(navigation.action_lines)),

        "go back <n>":
            R(Key("a-left")*Repeat(extra='n')),
        "go forward [<n>]":
            R(Key("a-right"))*Repeat(extra="n"),

        # Display
        "[toggle] full screen":
            R(Key("f11")),
        "flip layout":
            R(Key("sa-0")),
        "zoom in [<n>]":
            R(Key("c-equal")*Repeat(extra='n')),
        "zoom out [<n>]":
            R(Key("c-minus")*Repeat(extra='n')),
        "sidebar":
            R(Key("c-b")),
        "explore":
            R(Key("cs-e")),
        "source control":
            R(Key("cs-g")),
        "keyboard shortcuts":
            R(Key("c-k, c-s")),
        "key mappings":
            R(Key("c-k, c-s:2")),
        "settings":
            R(Key("a-f, p, s, enter")),
        "snippets":
            R(Key("a-f, p, s:2, enter")),
        "extensions":
            R(Key("cs-x")),
        "outline":
            R(Key("cs-o")),
        "search details":
            R(Key("cs-j")),
        "output panel":
            R(Key("cs-u")),
        "markdown preview":
            R(Key("cs-v")),
        "markdown preview side":
            R(Key("c-k, v")),
        "Zen mode":
            R(Key("c-k, z")),
        "toggle centered":
            R(Key("c-k, c-l")),
        "change theme":
            R(Key("c-k, c-t")),

        # File Management
        "copy path":
            R(Key("c-k, p")),
        "commander":
            R(Key("cs-p")),
        "go to [<text>]":
            R(Key("c-p") + Text("%(text)s")),
        "file open":
            R(Key("c-o")),
        "folder open":
            R(Key("c-k, c-o")),
        "save and close":
            R(Key("c-s/10, c-w")),
        "file new":
            R(Key("ca-n")),  # advanced-new-file extension
        "window new":
            R(Key("cs-n")),
        "window close":
            R(Key("a-f4")),
        "workspace close":
            R(Key("c-k, f")),
        "editor close":
            R(Key("c-f4")),
        "save as":
            R(Key("cs-s")),
        "save all":
            R(Key("c-k, s")),
        "preview close":
            R(Key("space, c-z")),
        "preview pin":
            R(Key("c-k, enter")),
        "explore here":
            R(Key("c-k, r")),
        "source commit":
            R(Key("c-enter")),

        # Search
        "replace":
            R(Key("c-h")),
        "search":
            R(Key("cs-f")),
        "search and replace":
            R(Key("cs-h")),
        "next find":
            R(Key("f3")),
        "(prior | previous) find":
            R(Key("s-f3")),
        "select all occurrences":
            R(Key("a-enter")),
        "toggle case sensitive":
            R(Key("a-c")),
        "toggle regex":
            R(Key("a-r")),
        "toggle whole word":
            R(Key("a-w")),
        "show all symbols":
            R(Key("c-t")),
        "go to symbol":
            R(Key("cs-o")),

        # Editor Management
        "tab close":
            R(Key("c-w")),
        "folder close":
            R(Key("c-k, f")),
        "window split":
            R(Key("c-backslash")),
        "group left":
            R(Key("c-k, left")),
        "group right":
            R(Key("c-k, right")),
        "<nth> tab":
            R(Key("a-%(nth)s")),

        # Languages Editing
        "go to definition":
            R(Key("f12")),
        "go to required definition":
            R(Key("c-f12:2, c-right:5, left/50, f12")),
        "peak definition":
            R(Key("a-f12")),
        "trigger parameter hints":
            R(Key("cs-space")),
        "format that":
            R(Key("c-k, c-f")),
        "(definition to side | side def)":
            R(Key("c-k, f12")),
        "show references":
            R(Key("s-f12")),
        "rename symbol":
            R(Key("f2")),
        "(trim white)":
            R(Key("c-k, c-x")),
        "change file language":
            R(Key("c-k, m")),

        # Debugging
        "debug":
            R(Key("cs-d")),
        "[toggle] break point":
            R(Key("f9")),
        "step over [<n>]":
            R(Key("f10/50")*Repeat(extra='n')),
        "step into":
            R(Key("f11")),
        "step out [of]":
            R(Key("s-f11")),
        "resume":
            R(Key("f5")),
        "stopper":
            R(Key("s-f5")),
        "continue":
            R(Key("f5")),
        "(show hover|mouse hover|hover mouse)":
            R(Key("c-k, c-i")),
        "[show] problems [panel]":
            R(Key("cs-m")),
        "next error":
            R(Key("f8")),  # doesn't seem to be working properly
        "(prior | previous) error":
            R(Key("s-f8")),
        "toggle tab moves focus":
            R(Key("c-m")),

        # Integrated Terminal
        "term new":
            R(Key("cs-backtick")),
        "term scroll up":
            R(Key("c-up")),
        "term scroll down":
            R(Key("c-down")),
        "term pinch":
            R(Key("s-pgup")),
        "term punch":
            R(Key("s-pgdown")),
        "nexterm":
            R(Key("cs-0")),
        "prexterm":
            R(Key("cs-9")),
        "term split":
            R(Key("c-backslash")),

        # Collapsing
        "fold region":
            R(Key("cs-lbracket")),
        "unfold region":
            R(Key("cs-rbracket")),
        "fold [all] subregions":
            R(Key("c-k, c-lbracket")),
        "unfold [all] subregions":
            R(Key("c-k, c-rbracket")),
        "fold [all] regions":
            R(Key("c-k, c-0")),
        "unfold [all] regions":
            R(Key("c-k, c-j")),
        "toggle word wrap":
            R(Key("a-z")),
        "run this line":
            R(Key("csa-l")),
        "join line":
            R(Key("csa-j")),

        # requires gitlens extension
        "toggle blame":
            R(Key("cs-g, b")),
        "lens commit details":
            R(Key("cs-g, c")),
        "lens file history":
            R(Key("cs-g, h")),
        "lens repo status":
            R(Key("cs-g, s")),
        "toggle git lens":
            R(Key("cs-g, s-b")),

        # requires bookmark extension
        # "mark (prev | prior | previous)":
        #     R(Key("ca-j")),
        # "mark next":
        #     R(Key("ca-l")),
    }
    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("ln1", 1, 1000),
        IntegerRefST("ln2", 1, 1000),
        IntegerRefST("n", 1, 1000),
        Choice("action", navigation.actions),
        Choice(
            "nth", {
                "first": "1",
                "second": "2",
                "third": "3",
                "fourth": "4",
                "fifth": "5",
                "sixth": "6",
            }),
    ]
    defaults = {"n": 1, "ln2": "", "mim": "", "text": ""}



class VSCodeCcrRule(MergeRule):
    pronunciation = "visual studio code continuous"
    mwith = CCRMerger.CORE
    non = VSCodeNonCcrRule

    mapping = {
        # Scrolling
        "scroll up [<n>]":
            R(Key("c-up") * Repeat(extra='n')),
        "scroll down [<n>]":
            R(Key("c-down") * Repeat(extra='n')),
        "scroll page up [<n>]":
            R(Key("a-pgup") * Repeat(extra='n')),
        "scroll page down [<n>]":
            R(Key("a-pgdown") * Repeat(extra='n')),

        # Line Manipulation
        "indent [<n>]":
            R(Key("c-rbracket") * Repeat(extra='n')),
        "(unindent|outdent) [<n>]":
            R(Key("c-lbracket") * Repeat(extra='n')),
        "comment":
            R(Key("c-slash")),
        "block comment":
            R(Key("sa-a")),
        "line delete [<n>]":
            R(Key("s-del") * Repeat(extra='n')),
        "switch up [<n>]":
            R(Key("a-up") * Repeat(extra='n')),
        "switch down [<n>]":
            R(Key("a-down") * Repeat(extra='n')),
        "copy up [<n>]":
            R(Key("csa-up") * Repeat(extra='n')),
        "copy down [<n>]":
            R(Key("csa-down") * Repeat(extra='n')),

        # Cursor
        "soft undo":
            R(Key("c-u")),
        "cursor all":
            R(Key("cs-l")),
        "cursor next [<n>]":
            R(Key("c-d") * Repeat(extra='n')),
        "cursor up [<n>]":
            R(Key("sa-up") * Repeat(extra='n')),
        "cursor down [<n>]":
            R(Key("sa-down") * Repeat(extra='n')),
        "cursor lines":
            R(Key("sa-i") * Repeat(extra='n')),
        "cursor bracket":
            R(Key("cs-backslash")),

        # Selection
        "expand [<n>]":
            R(Key("sa-right")) * Repeat(extra='n'),
        "shrink [<n>]":
            R(Key("sa-left")) * Repeat(extra='n'),

        # Stolen from above rule
        "show terminal":
            R(Key("c-backtick")),
        "toggle terminal":
            R(Key("c-backtick:2")),
        "pane next":
            R(Key("c-k, c-right")),
        "pane prior":
            R(Key("c-k, c-right")),
        "<m> pane":
            R(Key("c-%(m)s")),

        # Emmet
        "rip":
            R(Key("s-space")),
        "wrap tag":
            R(Key("c-e, w")),
        "update tag":
            R(Key("c-e, e")),
        "remove tag":
            R(Key("c-e, r")),
        "(split|join) tag":
            R(Key("c-e, s")),
        "next edit":
            R(Key("c-e, v")),
        "prior edit":
            R(Key("c-e, c")),

        # metaGo extension
        "hyper <letters>":
            R(Key("a-semicolon/5, %(letters)s")),
        "hyper select <letters>":
            R(Key("sa-semicolon/5, %(letters)s")),
        "select up [<n>]":
            R(Key("cs-i") * Repeat(extra='n')),
        "select down [<n>]":
            R(Key("c-i") * Repeat(extra='n')),
        "block up [<n>]":
            R(Key("a-home") * Repeat(extra='n')),
        "block down [<n>]":
            R(Key("a-end") * Repeat(extra='n')),
        "block select up [<n>]":
            R(Key("sa-home") * Repeat(extra='n')),
        "block select down [<n>]":
            R(Key("sa-end") * Repeat(extra='n')),
    }
    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 100),
        IntegerRefST("m", 1, 10),
        Choice("letters", caster_alphabet),
    ]

    defaults = {"n": 1, "mim": "", "text": ""}


context = AppContext(title="Visual Studio Code", executable="code")
control.ccr_app_rule(VSCodeCcrRule(), context)
