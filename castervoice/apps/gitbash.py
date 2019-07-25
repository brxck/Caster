from castervoice.lib.imports import *


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class GitBashRule(MergeRule):
    mapping = {
        "(git|get) base":
            Text("git "),
        "(git|get) (initialize repository|init)":
            Text("git init"),
        "(git|get) add":
            R(Text("git add .")),
        "(git|get) add all":
            R(Text("git add -A")),
        "(git|get) commit all":
            R(Mimic("git", "add", "all", "git", "commit")),
        "(git|get) status":
            R(Text("git status")),
        "(git|get) log":
            R(Text("git log")),
        "(git|get) log one line":
            R(Text("git log --oneline")),
        "(git|get) commit":
            R(Text("git commit -m \"\"") + Key("left")),
        "(git|get) bug fix commit <n>":
            R(Mimic("get", "commit") + Text("Fixes #%(n)d ") + Key("backspace")),
        "(git|get) reference commit <n>":
            R(Mimic("get", "commit") + Text("Refs #%(n)d ") + Key("backspace")),
        "(git|get) checkout":
            R(Text("git checkout ")),
        "(git|get) branch":
            R(Text("git branch ")),
        "(git|get) checkout branch":
            R(Text("git checkout -b ")),
        "(git|get) remote":
            R(Text("git remote ")),
        "(git|get) merge":
            R(Text("git merge ")),
        "(git|get) merge tool":
            R(Text("git mergetool")),
        "(git|get) rebase":
            R(Text("git rebase ")),
        "(git|get) fetch":
            R(Text("git fetch ")),
        "(git|get) push":
            R(Text("git push ")),
        "(git|get) push origin master":
            R(Text("git push origin master")),
        "(git|get) pull":
            R(Text("git pull ")),
        "CD up":
            R(Text("cd ..")),
        "CD":
            R(Text("cd ")),
        "LS":
            R(Text("ls")),
        "make directory":
            R(Text("mkdir ")),
        "undo [last] commit | (git|get) reset soft head":
            R(Text("git reset --soft HEAD~1")),
        "(undo changes | (git|get) reset hard)":
            R(Text("git reset --hard")),
        "stop tracking [file] | (git|get) remove":
            R(Text("git rm --cached ")),
        "preview remove untracked | (git|get) clean preview":
            R(Text("git clean -nd")),
        "remove untracked | (git|get) clean untracked":
            R(Text("git clean -fd")),
        "(git|get) visualize":
            R(Text("gitk")),
        "(git|get) visualize file":
            R(Text("gitk -- PATH")),
        "(git|get) visualize all":
            R(Text("gitk --all")),
        "(git|get) stash":
            R(Text("git stash")),
        "(git|get) stash apply [<n>]":
            R(Text("git stash apply") + Function(_apply)),
        "(git|get) stash list":
            R(Text("git stash list")),
        "(git|get) stash branch":
            R(Text("git stash branch NAME")),
        "(git|get) cherry pick":
            R(Text("git cherry-pick ")),
        "(git|get) (abort cherry pick | cherry pick abort)":
            R(Text("git cherry-pick --abort")),
        "(git|get) (GUI | gooey)":
            R(Text("git gui")),
        "(git|get) blame":
            R(Text("git blame PATH -L FIRSTLINE,LASTLINE")),
        "(git|get) gooey blame":
            R(Text("git gui blame PATH")),
        "search recursive":
            R(Text("grep -rinH \"PATTERN\" *")),
        "search recursive count":
            R(Text("grep -rinH \"PATTERN\" * | wc -l")),
        "search recursive filetype":
            R(Text("find . -name \"*.java\" -exec grep -rinH \"PATTERN\" {} \\;")),
        "to file":
            R(Text(" > FILENAME")),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {"n": 0}


terminal_context = AppContext(executable=[
    "gnome-terminal",
    "guake",
    "cool-retro-term",
    "hyper",
    "\\git-bash.exe"
])

jetbrains_context = AppContext(executable="idea", title="IntelliJ") \
    | AppContext(executable="idea64", title="IntelliJ") \
    | AppContext(executable="studio64") \
    | AppContext(executable="pycharm")

vs_code_context = AppContext(title="Visual Studio Code", executable="code")

context = terminal_context | jetbrains_context | vs_code_context

control.ccr_app_rule(GitBashRule(), context)
