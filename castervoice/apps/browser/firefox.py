from castervoice.lib.imports import *

import browser
from castervoice.apps.browser.browser_shared_commands import BrowserSharedCommands

class FirefoxRule(BrowserSharedCommands):
    pronunciation = "fire fox"

    _mapping = {
        browser.PREVIOUS_TAB_N_TIMES:
            # control shift tab doesn't work and this appears to be an undocumented workaround
            R(Key("c-tab/30")) * Repeat(extra="n"),
        browser.FIND_NEXT_MATCH:
            R(Key("c-g/20")) * Repeat(extra="n"),
        browser.TOGGLE_BOOKMARK_TOOLBAR:
            R(Key("c-b")),
        browser.SHOW_EXTENSIONS:
            R(Key("a-a, l, e/15, enter")),
        "dev network":
            R(Key("cs-e")),
        "dev console":
            R(Key("cs-k")),
        "dev element":
            R(Key("cs-c")),
        "dev style":
            R(Key("s-f7")),
        "dev profiler":
            R(Key("s-f5")),
        "dev responsive":
            R(Key("cs-m")),
        "dev storage":
            R(Key("s-f9")),
        }
    mapping = BrowserSharedCommands.merge_dictionaries(_mapping, BrowserSharedCommands.chromeAndFirefoxMapping)
    extras = browser.EXTRAS
    defaults = browser.DEFAULTS


context = AppContext(executable="firefox")
control.non_ccr_app_rule(FirefoxRule(), context=context)