'''
Created on July 29, 2019

@author: Brock McElroy
'''
from castervoice.lib.imports import *


class Terminal(MergeRule):
    pronunciation = "terminal"

    mapping = {
        "sudo": R(Text("sudo "), rdescript="Terminal: sudo"),
        "LS": R(Text("ls "), rdescript="Terminal: ls"),
        "CD": R(Text("cd "), rdescript="Terminal: cd"),
        "CD up": R(Text("cd .."), rdescript="Terminal: cd .."),
        "CD back": R(Text("cd -"), rdescript="Terminal: cd -"),
        "CD home": R(Text("cd -"), rdescript="Terminal: cd ~"),
        "PWD": R(Text("pwd"), rdescript="Terminal: pwd"),
        "make dir": R(Text("mkdir "), rdescript="Terminal: mkdir"),
        "touch": R(Text("touch "), rdescript="Terminal: touch"),
        "less": R(Text("less "), rdescript="Terminal: less"),
        "rim": R(Text("rm "), rdescript="Terminal: rm"),
        "rim raf": R(Text("rm -rf"), rdescript="Terminal: rm -rf"),
        "CP": R(Text("cp "), rdescript="Terminal: cp"),
        "MV": R(Text("mv "), rdescript="Terminal: mv"),
        "find": R(Text("find "), rdescript="Terminal: find"),
        "man": R(Text("man "), rdescript="Terminal: man"),
        "grep": R(Text("grep "), rdescript="Terminal: grep"),
        "history": R(Key("c-r"), rdescript="Terminal: Command History"),
        
        "dang": R(Text("fuck") + Key("enter"), rdescript="Terminal: fuck"),
        "micro": R(Text("micro"), rdescript="Terminal: micro"),
        "tldr": R(Text("tldr "), rdescript="Terminal: tldr"),

        "cut": R(Key("cs-x"), rdescript="Terminal: Cut"),
        "copy": R(Key("cs-c"), rdescript="Terminal: Copy"),
        "paste": R(Key("cs-v"), rdescript="Terminal: Paste"),
    }

    extras = [
        Dictation("text"),
    ]
    defaults = {}


control.global_rule(Terminal())
