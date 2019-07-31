from castervoice.lib.imports import *


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class GitBashRule(MergeRule):
    mapping = {
        "sudo":
            R(Text("sudo "), rdescript="Terminal: sudo"),
        "LS":
            R(Text("ls "), rdescript="Terminal: ls"),
        "CD":
            R(Text("cd "), rdescript="Terminal: cd"),
        "CD up":
            R(Text("cd .."), rdescript="Terminal: cd .."),
        "CD back":
            R(Text("cd -"), rdescript="Terminal: cd -"),
        "CD home":
            R(Text("cd -"), rdescript="Terminal: cd ~"),
        "PWD":
            R(Text("pwd"), rdescript="Terminal: pwd"),
        "make dir":
            R(Text("mkdir "), rdescript="Terminal: mkdir"),
        "touch":
            R(Text("touch "), rdescript="Terminal: touch"),
        "less":
            R(Text("less "), rdescript="Terminal: less"),
        "rim":
            R(Text("rm "), rdescript="Terminal: rm"),
        "rim raf":
            R(Text("rm -rf"), rdescript="Terminal: rm -rf"),
        "CP":
            R(Text("cp "), rdescript="Terminal: cp"),
        "MV":
            R(Text("mv "), rdescript="Terminal: mv"),
        "find":
            R(Text("find "), rdescript="Terminal: find"),
        "man":
            R(Text("man "), rdescript="Terminal: man"),
        "grep":
            R(Text("grep "), rdescript="Terminal: grep"),
        "history":
            R(Key("c-r"), rdescript="Terminal: Command History"),
        
        "dang":
            R(Text("fuck") + Key("enter"), rdescript="Terminal: fuck"),
        "micro":
            R(Text("micro"), rdescript="Terminal: micro"),
        "tldr":
            R(Text("tldr "), rdescript="Terminal: tldr"),

        "cut":
            R(Key("cs-x"), rdescript="Terminal: Cut"),
        "copy":
            R(Key("cs-c"), rdescript="Terminal: Copy"),
        "paste":
            R(Key("cs-v"), rdescript="Terminal: Paste"),

        # git
        "git base":
            Text("git "),
        "git (initialize repository|init)":
            Text("git init"),
        "git add":
            R(Text("git add .")),
        "git add all":
            R(Text("git add -A")),
        "git commit all":
            R(Mimic("git", "add", "all", "git", "commit")),
        "git status":
            R(Text("git status")),
        "git log":
            R(Text("git log")),
        "git log one line":
            R(Text("git log --oneline")),
        "git commit":
            R(Text("git commit -m \"\"") + Key("left")),
        "git bug fix commit <n>":
            R(Mimic("get", "commit") + Text("Fixes #%(n)d ") + Key("backspace")),
        "git reference commit <n>":
            R(Mimic("get", "commit") + Text("Refs #%(n)d ") + Key("backspace")),
        "git checkout <branch>":
            R(Text("git checkout %(branch)s")),
        "git branch":
            R(Text("git branch ")),
        "git checkout branch":
            R(Text("git checkout -b")),
        "git remote":
            R(Text("git remote ")),
        "git merge <branch>":
            R(Text("git merge %(branch)s")),
        "git merge tool":
            R(Text("git mergetool")),
        "git rebase":
            R(Text("git rebase ")),
        "git fetch":
            R(Text("git fetch ")),
        "git push <remote> <branch>":
            R(Text("git push %(remote)s %(branch)s")),
        "git pull <remote> <branch>":
            R(Text("git pull %(remote)s %(branch)s")),

        "undo [last] commit | git reset soft head":
            R(Text("git reset --soft HEAD~1")),
        "(undo changes | git reset hard)":
            R(Text("git reset --hard")),
        "stop tracking [file] | git remove":
            R(Text("git rm --cached ")),
        "preview remove untracked | git clean preview":
            R(Text("git clean -nd")),
        "remove untracked | git clean untracked":
            R(Text("git clean -fd")),

        "git visualize":
            R(Text("gitk")),
        "git visualize file":
            R(Text("gitk -- PATH")),
        "git visualize all":
            R(Text("gitk --all")),
        "git stash":
            R(Text("git stash")),
        "git stash apply [<n>]":
            R(Text("git stash apply") + Function(_apply)),
        "git stash list":
            R(Text("git stash list")),
        "git stash branch":
            R(Text("git stash branch NAME")),
        "git cherry pick":
            R(Text("git cherry-pick ")),
        "git (abort cherry pick | cherry pick abort)":
            R(Text("git cherry-pick --abort")),
        "git (GUI | gooey)":
            R(Text("git gui")),
        "git blame":
            R(Text("git blame PATH -L FIRSTLINE,LASTLINE")),
        "git gooey blame":
            R(Text("git gui blame PATH")),


    }
    extras = [
        IntegerRefST("n", 1, 10000),
        Choice("branch", {
            "master": "master",
            "develop": "develop",
        }),
        Choice("remote", {
            "origin": "origin",
            "upstream": "upstream"
        })
    ]
    defaults = {"n": 0}


terminal_context = AppContext(title="gnome-terminal") \
    | AppContext(title="guake")

context = terminal_context

control.ccr_app_rule(GitBashRule(), context)
