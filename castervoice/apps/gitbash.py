from castervoice.lib.imports import *


npm_commands = {
    "base": "",
    "build": "build",
    "ci": "ci",
    "explore": "explore",
    "init": "init",
    "install dev": "i --save-dev",
    "install": "i",
    "outdated": "outdated",
    "run build": "run build",
    "run develop": "run develop",
    "run dev": "run dev",
    "run": "run",
    "start": "start",
    "test": "test",
    "uninstall": "r",
    "update": "up",
}

git_commands = {
    "add all": "add -A",
    "add": "add",
    "base": "",
    "blame": "blame",
    "branch": "branch",
    "branch delete": "branch -d",
    "clone": "clone",
    "checkout": "checkout",
    "checkout branch": "checkout -b",
    "cherry pick abort": "cherry-pick --abort",
    "cherry pick": "cherry-pick",
    "clean preview": "clean -nd",
    "clean untracked": "clean -fd",
    "fetch": "fetch",
    "init": "init",
    "log one line": "log --oneline",
    "log": "log",
    "merge": "merge",
    "pull": "pull",
    "push": "push",
    "push upstream": "push -u",
    "rebase": "rebase",
    "remote": "remote",
    "remote add": "remote add",
    "remote remove": "remote rm",
    "remote list": "remote -v",
    "remove": "rm --cached",
    "reset hard": "reset --hard",
    "reset soft head": "reset --soft HEAD~1",
    "reset soft": "reset --soft",
    "stash apply": "stash apply",
    "stash branch": "stash branch",
    "stash clear": "stash clear",
    "stash list": "stash list",
    "stash": "stash",
    "status": "status",
}

django_command_list = ["check", "collect static", "dump data", "load data", "make migrations", "migrate",
                        "run server", "show migrations", "start app", "start project", "test", "create super user", "change password", "shell"]

django_commands = {command: command.replace(
    " ", "") + " " for command in django_command_list}

django_commands["shell plus"] = "shell_plus"
django_commands["manage"] = ""

vagrant_command_list = ["up", "resume", "provision",
                        "reload", "ssh", "halt", "suspend", "destroy", "status"]

vagrant_commands = {command: command for command in vagrant_command_list}


class GitBashRule(MergeRule):
    mapping = {
        "term close":
            R(Key("c-c")),
        "term quit":
            R(Key("c-d")),
        "term suspend":
            R(Key("c-z")),
        "term history":
            R(Key("c-r")),
        "whack":
            R(Key("c-w")),
        "undo":
            R(Text("")),
        "save":
            R(Text("")),

        "sudo":
            R(Text("sudo ")),
        "LS":
            R(Text("ls ")),
        "CD":
            R(Text("cd ")),
        "CD up":
            R(Text("cd ..")),
        "CD back":
            R(Text("cd -")),
        "home":
            R(Text("~/")),
        "PWD":
            R(Text("pwd")),
        "make dir":
            R(Text("mkdir ")),
        "touch":
            R(Text("touch ")),
        "less":
            R(Text("less ")),
        "RM":
            R(Text("rm ")),
        "RM RF":
            R(Text("rm -rf")),
        "CP":
            R(Text("cp ")),
        "MV":
            R(Text("mv ")),
        "find":
            R(Text("find ")),
        "man":
            R(Text("man ")),
        "grep":
            R(Text("grep ")),
        "ssh":
            R(Text("ssh ")),

        "slash home":
            R(Text("~/")),
        "slash up":
            R(Text("../")),
        "slash here":
            R(Text("./")),

        "dang":
            R(Text("fuck") + Key("enter")),
        "micro":
            R(Text("micro")),
        "tldr":
            R(Text("tldr ")),

        "cut":
            R(Key("cs-x")),
        "copy":
            R(Key("cs-c")),
        "spark":
            R(Key("cs-v")),

        "git <git_command>":
            R(Text("git %(git_command)s ")),
        "NPM <npm_command> ":
            R(Text("npm %(npm_command)s ")),
        "django <django_command>":
            R(Text("python manage.py %(django_command)s")),
        "vagrant <vagrant_command>":
            R(Text("vagrant %(vagrant_command)s ")),

        # Kitty
        "tab new":
            R(Key("cs-t")),
        "tab close":
            R(Key("cs-q")),
        "nexterm":
            R(Key("cs-right")),
        "prexterm":
            R(Key("cs-left")),
        "layout":
            R(Key("cs-l")),
        "pane new":
            R(Key("cs-enter")),
        "pane close":
            R(Key("cs-w")),
        "next pane":
            R(Key("cs-rbracket")),
        "prior pane":
            R(Key("cs-lbracket")),

        "pinch":
            R(Key("cs-pageup")),
        "punch":
            R(Key("cs-pagedown")),
    }

    extras = [
        IntegerRefST("n", 1, 10000),
        Choice("git_command", git_commands),
        Choice("npm_command", npm_commands),
        Choice("vagrant_command", vagrant_commands),
        Choice("django_command", django_commands)
    ]
    defaults = {"n": 0}


terminal_context = AppContext(title="gnome-terminal") \
    | AppContext(title="guake") \
    | AppContext(executable="kitty")

context = terminal_context

control.ccr_app_rule(GitBashRule(), context)
