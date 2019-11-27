# new modules should be added in the dictionary
# the tuple contains the rules which will be imported
from castervoice.lib import utilities

command_sets = {
    "core.alphabet": ("Alphabet", ),
    "core.nav": ("Navigation", ),
    "core.numbers": ("Numbers", ),
    "core.punctuation": ("Punctuation", ),
    "core.text_manipulation": ("TextManipulation", ),
    "voice_dev_commands.voice_dev_commands": ("VoiceDevCommands", ),
    "javascript.javascript": ("Javascript", ),
    "python.python": ("Python", ),
}

for module_name, class_name_tup in command_sets.iteritems():
    for class_name in class_name_tup:
        try:
            module = __import__(module_name, globals(), locals(),
                                [class_name])  # attempts to import the class
            globals()[class_name] = module  # make the name available globally

        except Exception as e:
            print("Ignoring ccr rule '{}'. Failed to load with: ".format(class_name))
            utilities.simple_log()
