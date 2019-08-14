#
# __author__ = "lexxish"
#
from castervoice.lib.imports import *

from castervoice.apps.shared.directions import FORWARD, RIGHT, BACK, LEFT

OPEN_NEW_WINDOW = "window new"
OPEN_NEW_INCOGNITO_WINDOW = "incognito new"
CLOSE_WINDOW = "win close"
NEW_TAB_N_TIMES = "tab new [<n>]"
REOPEN_TAB_N_TIMES = "tab restore [<n>]"
CLOSE_TAB_N_TIMES = "tab close [<n>]"
NEXT_TAB_N_TIMES = "nexta [<n>]"
PREVIOUS_TAB_N_TIMES = "prexta [<n>]"
OPEN_NEW_TAB_BASED_ON_CURSOR = "link new tab"
SWITCH_TO_TAB_N = "tab <n>"
SWITCH_TO_LAST_TAB = "tab last"
SWITCH_TO_SECOND_TO_LAST_TAB = "tab second last"
GO_FORWARD_N_TIMES = "go %s [<n>]" % FORWARD
GO_BACK_N_TIMES = "go %s [<n>]" % BACK
ZOOM_IN_N_TIMES = "zoom in [<n>]"
ZOOM_OUT_N_TIMES = "zoom out [<n>]"
ZOOM_RESET_DEFAULT = "zoom reset"
FORCE_HARD_REFRESH = "refresh hard"
FIND_NEXT_MATCH = "find %s [match] [<n>]" % FORWARD
FIND_PREVIOUS_MATCH = "find %s [match] [<n>]" % BACK
TOGGLE_CARET_BROWSING = "[toggle] caret browsing"
GO_TO_HOMEPAGE = "go home"
SHOW_HISTORY = "history"
SELECT_ADDRESS_BAR = "address bar"
PASTE_AND_GO = "paste and go"
NEW_TAB_AND_GO = "tab and go"
SHOW_DOWNLOADS = "downloads"
ADD_BOOKMARK = "bookmark tab"
BOOKMARK_ALL_TABS = "bookmark all"
TOGGLE_BOOKMARK_TOOLBAR = "bookmark bar"
SHOW_BOOKMARKS = "bookmarks"
TOGGLE_FULL_SCREEN = "full-screen"
SHOW_PAGE_SOURCE = "page source"
DEBUG_RESUME = "resume"
DEBUG_STEP_OVER = "step over"
DEBUG_STEP_INTO = "step into"
DEBUG_STEP_OUT = "step out"
DUPLICATE_TAB = "tab duplicate"
DUPLICATE_WINDOW = "window duplicate"
SHOW_EXTENSIONS = "extensions"
SHOW_MENU = "menu"
SHOW_SETTINGS = "settings"
SHOW_TASK_MANAGER = "task manager"
CLEAR_BROWSING_DATA = "history clear"
SHOW_DEVELOPER_TOOLS = "toolbox"
CHECKOUT_PR = "checkout [this] pull request [locally]"
UPDATE_PR = "update [this] pull request [locally]"

DEFAULTS = {"n": 1, "m": "", "nth": ""}
EXTRAS = [
    IntegerRefST("n", 1, 100),
    IntegerRefST("m", 1, 10)
]
